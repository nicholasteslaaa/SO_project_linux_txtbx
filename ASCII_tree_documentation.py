class Node:
    def __init__(self, name):
        self.parent = None
        self.name = name
        self.short_name = ""
        self.child_directories = []
        self.child_files = []
        self.edges = 0
        self.base = ""

    def build_tree(self, UBUNTU, depth, stacking):
        """
        --- input file system ---
        UBUNTU sebagai manuever
        depth sebagai indikator kapal selam
        stacking sebagai acuan kembali
        """
        if depth <= 0:
            return # berhenti sampai sini
        else:

            available_directories = UBUNTU.get_available_directories()
            for directory in available_directories:
                current_Node = Node(self.name + directory)
                self.child_directories.append(current_Node)

                current_Node.short_name = directory

                current_Node.edges = len(stacking)

                stacking.append(self.name + directory)
                UBUNTU.change_directory(stacking[-1])

                current_Node.child_files = UBUNTU.get_available_files()

                current_Node.build_tree(UBUNTU, depth - 1, stacking)
                UBUNTU.change_directory(stacking.pop())

    def traverse(self):
        for directory in self.child_directories:
            print(f'{directory.name}  {directory.edges}\n')
            print(f'{directory.child_files}')
            directory.traverse()

    def pipe_edges(self, depth):
        """
        GAGAL, saya tidak sadar ada edge case
        """
        panjang_space = 3
        for _ in range(depth - 1):
            self.base += str('|' + ' ' * panjang_space + "")
            print('|' + ' ' * panjang_space,end="")

    def new_pipe(self, lst, file):
        for x in lst:
            if x is True:
                file.write('|' + ' ' * 3 + " ")
            else:
                file.write(' ' * 4 + " ")

    def pretty_printing_files(self, lst, file):
        if self.child_files:
            for (j, file_name) in enumerate(self.child_files):
                self.new_pipe(lst, file)
                if j == len(self.child_files) - 1:
                    file.write(f'└── {file_name}\n')
                else:
                    file.write(f'├── {file_name}\n')

            self.new_pipe(lst, file)
            file.write('\n')
        else:
            if not self.child_directories:
                self.new_pipe(lst, file)
                file.write('\n')


    def pretty_printing_directories(self, lst, file):
        for (i, directory) in enumerate(self.child_directories):
            directory.new_pipe(lst, file)
            
            if i == len(self.child_directories) - 1:
                if not self.child_files:
                    file.write(f'└── {directory.short_name}\n')
                    lst.append(False)
                else:
                    file.write(f'├── {directory.short_name}\n')
                    lst.append(True)
            else:
                file.write(f'├── {directory.short_name}\n')
                lst.append(True)
            
            directory.pretty_printing_directories(lst, file)
            directory.pretty_printing_files(lst, file)
            lst.pop()


def tembelek(UBUNTU, depth, output_file_path='output.txt'):
    if depth == 0: depth = float('inf')
    root = Node(UBUNTU.get_current_path() + '/')
    root.child_files = UBUNTU.get_available_files()

    stacking = [root.name]
    with open(output_file_path, 'w') as file:
        root.build_tree(UBUNTU, depth, stacking)
        file.write(f'{root.name}\n')
        file.write('|\n')
        root.pretty_printing_directories([], file)
        # root.pretty_printing_files([], file)
    UBUNTU.change_directory(root.name)

# if __name__ == "__main__":
#     from 
#     ubuntu = LinuxOS()
#     current_path = ubuntu.get_current_path().split("/")
#     dest = "projectSO_linux"
#     if dest not in current_path:
#         current_path.append(dest)
#     current_path = "/".join(current_path)
#     print(current_path)
#     tembelek(ubuntu,3,f"{current_path}/output.txt")