from central_function import LinuxOS
# from ASCII_tree_documentation import tembelek
import tkinter as tk
class util:
    def __init__(self):
        self.ubuntu = LinuxOS()
        # self.show_currrent_path_enabled = False
        # self.curpathButton = None
        
        # self.show_avdir_enabled = False
        # self.avdirButton = None
        
        self.show_changedir_enabled = False
        self.changedirButton = None
        
        self.show_getText_enabled = False
        self.getTextButton = None
        
        self.curpath = self.ubuntu.get_current_path()
        self.avdir = "".join(self.ubuntu.get_available_directories())
        
        
    def util_btn(self, window, performances_label, graph_label,text_box):
        # self.curpath_btn(window, performances_label, graph_label,text_box)
        # self.avdir_btn(window, performances_label, graph_label,text_box)
        self.changedir_btn(window, performances_label, graph_label,text_box)
    
    def clearing(self, performances_label, graph_label,text_box):
        self.remove_getTextButton_btn()
        text_box.grid_forget()
        performances_label.config(text="")
        graph_label.config(text="")
        
        
    ############### current path ###############

    # def update_curpath(self, performances_label, graph_label,text_box):
    #     self.clearing(performances_label, graph_label,text_box)
    #     run_command = self.ubuntu.get_current_path()
    #     text_label = f"current path: {run_command}"
    #     performances_label.config(text = text_label , width = len(text_label)-5)

    # def curpath_btn(self, window, performances_label, graph_label,text_box):
    #     if self.curpathButton is None:  # Check if the button exists
    #         self.curpathButton = tk.Button(window, width=15, height=1, text='current path', borderwidth=2, relief='ridge', 
    #                                     command=lambda: self.update_curpath(performances_label, graph_label,text_box))
    #         self.curpathButton.grid(row=0, column=1)
    #     else:
    #         self.curpathButton.grid(row=0, column=1)

    # def remove_curpath_btn(self):
    #     if self.curpathButton is not None:
    #         self.curpathButton.grid_forget()  # Hide the button
    #         self.curpathButton = None  # Reset the button reference    
    
    
    # ############### avalable directory ###############
    # def update_avdir(self, performances_label, graph_label,text_box):
    #     self.clearing(performances_label, graph_label,text_box)
    #     run_command = self.ubuntu.get_available_directories()
    #     text_label = f"available directories: {''.join(run_command)}"
    #     performances_label.config(text = text_label , width = len(text_label))
    #     performances_label.grid(columnspan=len(text_label))


    # def avdir_btn(self, window, performances_label, graph_label,text_box):
    #     if self.avdirButton is None:  # Check if the button exists
    #         self.avdirButton = tk.Button(window, width=15, height=1, text='available directory', borderwidth=2, relief='ridge', 
    #                                     command=lambda: self.update_avdir(performances_label, graph_label,text_box))
    #         self.avdirButton.grid(row=0, column=2)
    #     else:
    #         self.avdirButton.grid(row=0, column=2)

    # def remove_avdir_btn(self):
    #     if self.avdirButton is not None:
    #         self.avdirButton.grid_forget()  # Hide the button
    #         self.avdirButton = None  # Reset the button reference   
    
    ############### change directory ###############
    
    def update_changedir(self,window,performances_label, graph_label,text_box):
        self.clearing(performances_label, graph_label,text_box)
        # run_command = self.ubuntu.change_directory()
        performances_label.config(text="")
        # performances_label.grid_forget()
        show_curpath = f"current path: {self.curpath}\navailable directory: {self.avdir}"
        graph_label.config(height=2,width=62,text=show_curpath,justify="left")
        graph_label.grid(row=1,column=1,columnspan=len(show_curpath),rowspan=10)

        text_box.grid(row=1, column=1, columnspan=2, rowspan=1)
        self.getText_btn(window,performances_label,graph_label,text_box)
        # text_label = f"available directories: {''.join(run_command)}"
        # performances_label.config(text = text_label , width = len(text_label)-5)

    def changedir_btn(self, window, performances_label, graph_label,text_box):
        if self.changedirButton is None:  # Check if the button exists
            self.changedirButton = tk.Button(window, width=15, height=1, text='change directory', borderwidth=2, relief='ridge', 
                                        command=lambda:self.update_changedir(window,performances_label, graph_label,text_box))
            self.changedirButton.grid(row=0, column=1)
        else:
            self.changedirButton.grid(row=0, column=1)
    
    def getText_btn(self, window, performances_label, graph_label,text_box):
        if self.getTextButton is None:  # Check if the button exists
            self.getTextButton = tk.Button(window, width=10, height=1, text='change directory', borderwidth=2, relief='ridge',command=lambda:self.get_text(graph_label,text_box))
            self.getTextButton.grid(row=1, column=3)
        else:
            self.getTextButton.grid(row=1, column=3)
            
    def get_text(self,graph_label,text_box):
        # Retrieve the content of the text box
        # current_path = ubuntu.get_current_path().split("/")
        # dest = "yes"
        # if dest not in current_path:
        #     current_path.append(dest)
        # current_path = "/".join(current_path)+"/output.txt"
        content = text_box.get("1.0", "end-1c")
        print("Text box content:", content)
        self.ubuntu.change_directory(content)
        self.curpath = self.ubuntu.get_current_path()
        self.avdir = "".join(self.ubuntu.get_available_directories())
        show_curpath = f"current path: {self.curpath}\navailable directory: {self.avdir}"
        graph_label.config(text=show_curpath)
        graph_label.grid(columnspan=len(show_curpath))

    def remove_changedir_btn(self):
        if self.changedirButton is not None:
            self.changedirButton.grid_forget()  # Hide the button
            self.changedirButton = None  # Reset the button reference
    def remove_getTextButton_btn(self):
        if self.getTextButton is not None:
            self.getTextButton.grid_forget()  # Hide the button
            self.getTextButton = None  # Reset the button reference
        
    
    
    ############### else button ###############
    def elsebtn(self, performances_label, graph_label):
        self.show_available_directory_enabled = False
        performances_label.config(text="")
        graph_label.config(text="")
        # self.remove_curpath_btn()
        # self.remove_avdir_btn()
        self.remove_changedir_btn()
        self.remove_getTextButton_btn()