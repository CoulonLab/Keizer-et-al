from scipy import *

__version__='1.5'

class dataset:
    def __init__(self, fname, tPull=0., tRelease=None, nbFramesForBaseline_pull=1, nbFramesForBaseline_release=1, fnameDistNE=None):
        ## If `tPull` is - a scalar => this value is usd as the time t=0 of the pull
        ##               - a list of integers => the mean time over the corresionding
        ##                 frames is used as t=0. E.g. [99] implies that t=0 is frame 99
        ##                 or [34,35] implies that t=0 is between frames 34 and 35.
        ## If `tRelease` is `None`, no release is considered. If it is a scalar or a list
        ##                 of integers, the same principle as for `tPull` applies.
        ## `nbFramesForBaseline_pull` and `nbFramesForBaseline_release` indicate the number
        ##                 of frames that should be used to cumpute the (0,0,0) position of
        ##                 the pull and the release.
        ## `fnameDistNE` (optional) is the name of the file containing measurements of
        ##                 distance to the nuclear envelope.
        
        self.fname = fname
        self.fnameDistNE = fnameDistNE

        # Load trajectory datafile
        try:
            self._data_full = loadtxt(fname, delimiter='\t',skiprows=1)
        except:
            self._data_full = loadtxt(fname,skiprows=1)
            
        # Load distance to nuclear envelope datafile
        if not self.fnameDistNE is None:
            self._dataDistNE_full = loadtxt(self.fnameDistNE)
            # Check that trajectory and distNE files are compatible
            if not (self._data_full.shape[0]==self._dataDistNE_full.shape[0]
                    and not sum(isnan(self._dataDistNE_full[invert(isnan(self._data_full[:,0]))]))):
                raise ValueError("Provided `fname` and `fnameDistNE` files are not compatible.")
            # Combine tables
            self._data_full=c_[self._data_full,self._dataDistNE_full[:,1:3]]
            
        # Clean up nans
        self._data = self._data_full[logical_not(any(isnan(self._data_full[:,4:6]),axis=1))]
        
        # Determine tPull and tRelease if provided as (list of) frames
        if type(tPull)    in [list, tuple]: tPull   =self._data_full[tPull,0].mean()
        if type(tRelease) in [list, tuple]: tRelease=self._data_full[tRelease,0].mean()-tPull
        
        ## *Measured* timestamps, Force and position
        self.t = self.t_m = self._data[:, 0] - tPull
        self.F = self.F_m = self._data[:, 1:4]  * r_[1,-1,-1]
        self.x = self.x_m = self._data[:, 7:10] * r_[1,-1,-1]
        
        # Infer and add position and force at t=0- and t=0+ (Force ON)
        # => use mean of the `nbFramesForBaseline_pull` last known position
        ind = where(self.t > 0)[0][0]
        self.t = insert(self.t, ind, 0,                                                axis=0) # t=0+
        self.x = insert(self.x, ind, self.x[:ind][-nbFramesForBaseline_pull:].mean(0), axis=0)
        self.F = insert(self.F, ind, self.F[:ind][-nbFramesForBaseline_pull:].mean(0), axis=0)
        self.t = insert(self.t, ind, -0.01,                                            axis=0) # t=0-
        self.x = insert(self.x, ind, self.x[:ind][-nbFramesForBaseline_pull:].mean(0), axis=0) 
        self.F = insert(self.F, ind, 0,                                                axis=0)
        self.indON   = ind+1
        self.indON_m = ind
        # Set force to 0 before t=0
        self.F  [:self.indON  ] = 0.
        self.F_m[:self.indON_m] = 0.

        # Infer and add position and force at t=tRelease- and t=tRelease+ (Force OFF)
        #   => use mean of `nbFramesForBaseline_release` last known position
        if tRelease!=None and any(self.t>tRelease):
            self.tRelease=tRelease
            ind = where(self.t > tRelease)[0][0]
            self.t = insert(self.t, ind, tRelease+0.01,                                       axis=0) # t=tRelease+
            self.x = insert(self.x, ind, self.x[:ind][-nbFramesForBaseline_release:].mean(0), axis=0)
            self.F = insert(self.F, ind, 0,                                                   axis=0)
            self.t = insert(self.t, ind, tRelease,                                            axis=0) # t=tRelease-
            self.x = insert(self.x, ind, self.x[:ind][-nbFramesForBaseline_release:].mean(0), axis=0) 
            self.F = insert(self.F, ind, self.F[:ind][-nbFramesForBaseline_release:].mean(0), axis=0)
            self.indOFF   = ind+1
            self.indOFF_m = ind-2
            # Set force to 0 after t=tRelsease
            self.F  [self.indOFF:  ] = 0.
            self.F_m[self.indOFF_m:] = 0.
        
        # Use position at t=0 as origin
        self.x_m-=self.x[self.indON]
        self.x  -=self.x[self.indON]

