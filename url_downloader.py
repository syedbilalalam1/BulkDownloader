import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import requests
import os
from urllib.parse import urlparse
from threading import Thread
from ttkthemes import ThemedTk

class URLDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("Batch URL Downloader")
        self.root.geometry("700x500")
        
        # Set theme
        self.root.configure(bg='#f0f0f0')
        style = ttk.Style()
        style.configure("Custom.TFrame", background='#f0f0f0')
        style.configure("Custom.TLabel", background='#f0f0f0', font=('Helvetica', 10))
        style.configure("Title.TLabel", background='#f0f0f0', font=('Helvetica', 14, 'bold'))
        style.configure("Credits.TLabel", background='#f0f0f0', font=('Helvetica', 8), foreground='#666666')
        
        # Create main frame
        self.main_frame = ttk.Frame(self.root, padding="20", style="Custom.TFrame")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        self.title_label = ttk.Label(self.main_frame, text="Batch URL Downloader", style="Title.TLabel")
        self.title_label.grid(row=0, column=0, columnspan=2, sticky=tk.W, pady=(0, 20))
        
        # URL input area
        self.url_label = ttk.Label(self.main_frame, text="Enter URLs (one per line):", style="Custom.TLabel")
        self.url_label.grid(row=1, column=0, sticky=tk.W, pady=(0, 5))
        
        # Create a frame for the text area with border
        self.text_frame = ttk.Frame(self.main_frame, borderwidth=1, relief="solid")
        self.text_frame.grid(row=2, column=0, columnspan=2, pady=(0, 20), sticky=(tk.W, tk.E))
        
        self.url_text = tk.Text(self.text_frame, height=10, width=70, font=('Helvetica', 10))
        self.url_text.pack(padx=1, pady=1)
        
        # Download location
        self.location_label = ttk.Label(self.main_frame, text="Download Location:", style="Custom.TLabel")
        self.location_label.grid(row=3, column=0, sticky=tk.W, pady=(0, 5))
        
        self.location_var = tk.StringVar()
        self.location_entry = ttk.Entry(self.main_frame, textvariable=self.location_var, width=60)
        self.location_entry.grid(row=4, column=0, sticky=tk.W, padx=(0, 10))
        
        self.browse_button = ttk.Button(self.main_frame, text="Browse", command=self.browse_location)
        self.browse_button.grid(row=4, column=1, padx=5)
        
        # Progress bar
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(self.main_frame, variable=self.progress_var, maximum=100)
        self.progress_bar.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=20)
        
        # Status label
        self.status_var = tk.StringVar(value="Ready")
        self.status_label = ttk.Label(self.main_frame, textvariable=self.status_var, style="Custom.TLabel")
        self.status_label.grid(row=6, column=0, columnspan=2, sticky=tk.W)
        
        # Download button
        self.download_button = ttk.Button(self.main_frame, text="Start Download", command=self.start_download)
        self.download_button.grid(row=7, column=0, columnspan=2, pady=20)
        
        # Credits
        self.credits_label = ttk.Label(self.main_frame, 
                                     text="Made by syedbilalalam\nDiscord: bilalwastaken #9773", 
                                     style="Credits.TLabel",
                                     justify="center")
        self.credits_label.grid(row=8, column=0, columnspan=2, pady=(10, 0))
        
        # Set default download location
        self.location_var.set(os.path.join(os.path.expanduser("~"), "Downloads"))
        
        # Configure grid weights
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

    def browse_location(self):
        directory = filedialog.askdirectory()
        if directory:
            self.location_var.set(directory)

    def start_download(self):
        urls = self.url_text.get("1.0", tk.END).strip().split("\n")
        urls = [url.strip() for url in urls if url.strip()]
        
        if not urls:
            messagebox.showerror("Error", "Please enter at least one URL")
            return
            
        download_path = self.location_var.get()
        if not os.path.exists(download_path):
            messagebox.showerror("Error", "Invalid download location")
            return
            
        self.download_button.state(['disabled'])
        Thread(target=self.download_files, args=(urls, download_path)).start()

    def download_files(self, urls, download_path):
        total_files = len(urls)
        completed = 0
        
        for url in urls:
            try:
                self.status_var.set(f"Downloading: {url}")
                response = requests.get(url, stream=True)
                response.raise_for_status()
                
                # Get filename from URL
                filename = os.path.basename(urlparse(url).path)
                if not filename:
                    filename = "downloaded_file_" + str(completed + 1)
                
                file_path = os.path.join(download_path, filename)
                
                with open(file_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                
                completed += 1
                self.progress_var.set((completed / total_files) * 100)
                
            except Exception as e:
                messagebox.showerror("Error", f"Failed to download {url}\nError: {str(e)}")
        
        self.status_var.set("Download completed!")
        self.download_button.state(['!disabled'])
        messagebox.showinfo("Success", "All downloads completed!")

if __name__ == "__main__":
    root = ThemedTk(theme="arc")
    app = URLDownloader(root)
    root.mainloop() 