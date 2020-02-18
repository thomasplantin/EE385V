import mne
import scipy
from scipy import io
from mne import Epochs
from mne.channels import Layout
import os
from pathlib import Path

class EEGLib:

    def open(self, filepath):
        '''
        @param filepath: Path to GDF or .MAT file
        @:return Tuple (gdf, mat)
        '''

        path = Path(filepath)

        gdf_path = os.path.basename(filepath)
        mat_path = os.path.basename(filepath)
        if path.suffix == '.gdf':
            gdf_path = filepath
            mat_path = str(path.parent) + '/' + str(path.stem) + '.mat'
        elif path.suffix == '.mat':
            mat_path = filepath
            gdf_path = str(path.parent) + '/' + str(path.stem) + '.gdf'
        else:
            raise IOError('Filepath needs to be either a .gdf or .mat file')

        gdf = mne.io.read_raw_gdf(gdf_path, preload=True)
        mat = io.loadmat(mat_path)
        return (gdf, mat)


if __name__ == "__main__":
    e = EEGLib()
    (gdf, mat) = e.open('/home/amcelroy/Code/EE385V/BCI Course 2020/ErrPSpeller/Subject1/Offline/ad4_raser_offline_offline_171110_170617.gdf')
    print(g.info)