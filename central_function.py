import os
import shutil
import tempfile

class LinuxOS:
    def __init__ (self):

        # menangkap semua directory di 
        # path saat ini ( hanya directory )
        self.ls_dir = "ls -d */"

        # menampilkan path saat ini
        self.pwd = "pwd"

        # menangkap file-file di
        # path saat ini
        self.ls_file = "ls -p | grep -v /"

    def get_current_path(self):
        """
        return path directory saat ini
        """
        run_command = os.popen(self.pwd)
        read_command = run_command.read().rstrip()
        return read_command


    def change_directory(self, target_directory):
        """
        pindah dari directory saat ini
        ke directory target
        """
        try:
            os.chdir(target_directory)
        except:
            print("/directory tujuan tidak ada")


    def get_available_directories(self):
        """
        return semua directory pada working directory jika ada
        return empty [] jika tidak ada
        """
        run_command = os.popen(self.ls_dir)
        read_command = run_command.read().rstrip()
        lst_directories = read_command.split('\n')

        if ''.join(lst_directories) == "":
            return []
        else:
            return lst_directories

    
    def get_available_files(self):
        """
        return semua file-file pada working diretory jika ada
        return empty [] jika tidak ada
        """
        run_command = os.popen(self.ls_file)
        read_command = run_command.read().rstrip()
        lst_files = read_command.split('\n')

        if "".join(lst_files) == "":
            return []
        else:
            return lst_files


class PenghapusSementara:
    def __init__(self):
        self.direktori_sementara = tempfile.gettempdir()
        self.jumlah_file_dihapus = 0
        self.jumlah_folder_dihapus = 0

    def hapus_file_di_sementara(self):
        daftar_file = os.listdir(self.direktori_sementara)

        if not daftar_file:
            print("Tidak ada file sementara yang perlu dihapus.")
            return

        for nama_file in daftar_file:
            jalur_file = os.path.join(self.direktori_sementara, nama_file)
            try:
                if os.path.isfile(jalur_file) or os.path.islink(jalur_file):
                    os.unlink(jalur_file)
                    self.jumlah_file_dihapus += 1
                elif os.path.isdir(jalur_file):
                    shutil.rmtree(jalur_file)
                    self.jumlah_folder_dihapus += 1
            except Exception as e:
                print(f"Gagal menghapus {jalur_file}. Alasan: {e}")

        print(f"\nJumlah file yang dihapus: {self.jumlah_file_dihapus}")
        print(f"Jumlah folder yang dihapus: {self.jumlah_folder_dihapus}")

    def hapus_file_sementara(self):
        print(f"Lokasi folder sementara: {self.direktori_sementara}")
        
        konfirmasi = input(f"Apakah Anda yakin ingin menghapus semua file di {self.direktori_sementara}? (y/n): ").lower()
        if konfirmasi == 'y':
            self.hapus_file_di_sementara()
            print("Penghapusan file sementara selesai.")
        else:
            print("Penghapusan dibatalkan.")
            
            
if __name__ == "__main__":
    test = LinuxOS()
    print(test.get_current_path())
    print(test.get_available_directories())
    print(test.get_available_directories())