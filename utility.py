from central_function import LinuxOS
# from ASCII_tree_documentation import tembelek
import tkinter as tk
class util:
    def __init__(self):
        self.ubuntu = LinuxOS()
        
        self.show_changedir_enabled = False
        self.changedirButton = None
        
        self.show_getText_enabled = False
        self.getTextButton = None
        
        self.curpath = self.ubuntu.get_current_path()
        self.avdir = "".join(self.ubuntu.get_available_directories())
        
        
    def util_btn(self, window, performances_label, graph_label,text_box):
        self.changedir_btn(window, performances_label, graph_label,text_box)
    
    def clearing(self, performances_label, graph_label,text_box):
        self.remove_getTextButton_btn(text_box)
        text_box.grid_forget()
        performances_label.config(text="")
        graph_label.config(text="")

    ############### change directory ###############
    
    def update_changedir(self,window,performances_label, graph_label,text_box):
        self.clearing(performances_label, graph_label,text_box)
        performances_label.config(text="")
        show_curpath = f"current path: {self.curpath}\navailable directory: {self.avdir}"
        graph_label.config(height=2,width=62,text=show_curpath,justify="left")
        graph_label.grid(row=1,column=1,columnspan=len(show_curpath),rowspan=10)

        text_box.grid(row=1, column=1, columnspan=2, rowspan=1)
        self.getText_btn(window,graph_label,text_box)

    def changedir_btn(self, window, performances_label, graph_label,text_box):
        if self.changedirButton is None:  # Check if the button exists
            self.changedirButton = tk.Button(window, width=15, height=1, text='change directory', borderwidth=2, relief='ridge', 
                                        command=lambda:self.update_changedir(window,performances_label, graph_label,text_box))
            self.changedirButton.grid(row=0, column=1)
        else:
            self.changedirButton.grid(row=0, column=1)
    
    def getText_btn(self, window,graph_label,text_box):
        if self.getTextButton is None:  # Check if the button exists
            self.getTextButton = tk.Button(window, width=13, height=1, text='change directory', borderwidth=2,command=lambda:self.get_text(graph_label,text_box))
            self.getTextButton.grid(row=1, column=3)
        else:
            self.getTextButton.grid(row=1, column=3)
            
    def get_text(self,graph_label,text_box):
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
    def remove_getTextButton_btn(self,text_box):
        text_box.grid_forget()
        if self.getTextButton is not None:
            self.getTextButton.grid_forget()  # Hide the button
            self.getTextButton = None  # Reset the button reference
        
    
    
    ############### else button ###############
    def elsebtn(self, performances_label, graph_label,text_box):
        self.show_available_directory_enabled = False
        performances_label.config(text="")
        graph_label.config(text="")
        self.remove_changedir_btn()
        self.remove_getTextButton_btn(text_box)