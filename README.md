# C-For-Python-Dev
A repo holding some basic implementation of c with python to make your code almost 1000x faster

# **💻 GCC Compiler Installation Guide**

The GNU Compiler Collection (GCC) is a powerful, open-source compiler that supports multiple programming languages, including C, C++, and Fortran.

Use the links below to quickly navigate to the installation instructions for your operating system:

* [Windows Installation](https://www.google.com/search?q=%23windows-installation)  
  * [Method 1: Using MinGW-w64 (Recommended)](https://www.google.com/search?q=%23method-1-using-mingw-w64-recommended)  
  * [Method 2: Using WSL (Windows Subsystem for Linux)](https://www.google.com/search?q=%23method-2-using-wsl-windows-subsystem-for-linux)  
* [macOS Installation](https://www.google.com/search?q=%23macos-installation)  
  * [Method 1: Installing Xcode Command Line Tools](https://www.google.com/search?q=%23method-1-installing-xcode-command-line-tools)  
  * [Method 2: Using Homebrew](https://www.google.com/search?q=%23method-2-using-homebrew)  
* [Linux Installation](https://www.google.com/search?q=%23linux-installation)  
  * [Debian/Ubuntu (apt)](https://www.google.com/search?q=%23debianubuntu-apt)  
  * [Fedora/RHEL/CentOS (dnf/yum)](https://www.google.com/search?q=%23fedora-rhel-centos-dnf-yum)  
  * [Arch Linux (pacman)](https://www.google.com/search?q=%23arch-linux-pacman)

## **Windows Installation**

Since GCC is not native to Windows, you must install a port. The two most common and recommended methods are **MinGW-w64** (Minimalist GNU for Windows) or using **WSL**.

### **Method 1: Using MinGW-w64 (Recommended)**

MinGW-w64 provides a native Windows environment for developing GNU programs, including GCC.

1. **Download MinGW-w64:** Go to the official MinGW-w64 download page (or a reputable mirror like SourceForge) and download the installer or a pre-built zip file. The installer will guide you through choosing the architecture (usually x86\_64 for 64-bit systems).  
2. **Installation:**  
   * If you used the installer, follow the on-screen prompts. Ensure you select the necessary compiler components (like mingw32-gcc-g++ for C/C++ support).  
   * If you downloaded an archive, extract it to a simple, easy-to-access location, such as C:\\mingw64.  
3. **Set Environment Variables (Crucial Step):** To use GCC from any command prompt, you must add its location to the system's Path variable.  
   * Search for "Environment Variables" in the Windows Start menu and select **"Edit the system environment variables."**  
   * Click the **"Environment Variables..."** button.  
   * Under "System variables," find and select the **Path** variable, then click **"Edit."**  
   * Click **"New"** and add the path to the bin folder within your MinGW installation. For example: C:\\mingw64\\bin.  
   * Click **"OK"** to close all windows.  
4. **Verify Installation:** Open a new Command Prompt or PowerShell window and run:  
   gcc \--version

   If successful, it will display the GCC version information.

### **Method 2: Using WSL (Windows Subsystem for Linux)**

If you prefer a full Linux command-line environment on Windows, WSL is an excellent choice.

1. **Enable WSL:** Open PowerShell as an Administrator and run the installation command (this also installs Ubuntu by default):  
   wsl \--install

2. **Open WSL Terminal:** After restarting your computer (if required), open the Ubuntu/WSL terminal.  
3. **Install build-essential:** This package includes the GCC compiler, G++, and the make utility.  
   sudo apt update  
   sudo apt install build-essential

4. **Verify Installation:**  
   gcc \--version

## **macOS Installation**

On macOS, the easiest way to get the core GCC and C++ compiler (clang is the Apple default, but GCC can be installed) is through the Xcode Command Line Tools or the Homebrew package manager.

### **Method 1: Installing Xcode Command Line Tools (Provides clang, which acts as gcc for C/C++ by default)**

For most developers, installing the Command Line Tools is sufficient, as it includes the necessary compilers and development utilities.

1. **Open Terminal:** Open the Terminal application.  
2. **Run the install command:**  
   xcode-select \--install

3. **Follow Prompts:** A software update window will appear. Click **Install** and accept the license agreement.  
4. **Verify Installation:** Once complete, running the following command will show the version of the compiler (often Clang, but compatible with most GCC flags):  
   gcc \--version

### **Method 2: Using Homebrew (To install the official GNU GCC)**

If you need the specific GNU GCC suite (e.g., for compatibility with specific projects or Fortran), Homebrew is the preferred method.

1. **Install Homebrew (if you haven't already):**  
   /bin/bash \-c "$(curl \-fsSL \[https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh\](https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh))"

2. **Install GCC:** Use Homebrew to install the official GCC compiler. Homebrew often installs the latest stable version and names it with a version suffix (e.g., gcc-13 or g++-13).  
   brew install gcc

3. **Verify Installation:** Check the installed version. Note that you may need to use the version-suffixed name (gcc-13).  
   gcc \--version  
   \# or  
   g++-13 \--version 

## **Linux Installation**

On almost all modern Linux distributions, GCC is installed via the native package manager. The best practice is to install the build-essential package (or its equivalent), which includes GCC, G++, and other essential building utilities.

### **Debian/Ubuntu (apt)**

1. **Update Package Lists:**  
   sudo apt update

2. **Install build-essential:**  
   sudo apt install build-essential

3. **Verify Installation:**  
   gcc \--version

### **Fedora/RHEL/CentOS (dnf/yum)**

These distributions use dnf (newer) or yum (older) as their package manager.

1. **Update System:**  
   sudo dnf update  
   \# or (for older systems)  
   sudo yum update

2. **Install GCC and supporting tools:**  
   sudo dnf install gcc gcc-c++ make

3. **Verify Installation:**  
   gcc \--version

### **Arch Linux (pacman)**

1. **Synchronize Package Lists:**  
   sudo pacman \-Sy

2. **Install gcc and base-devel (for make and other tools):**  
   sudo pacman \-S gcc base-devel

3. **Verify Installation:**  
   gcc \--version

### **Test Your Installation**

To ensure your compiler is fully functional, create a simple hello.c file:

\#include \<stdio.h\>

int main() {  
    printf("Hello, GCC World\!\\n");  
    return 0;  
}

1. **Compile:**  
   gcc hello.c \-o hello

2. **Run (Linux/macOS):**  
   ./hello

3. **Run (Windows):**  
   .\\hello.exe

The output should be: Hello, GCC World\!

This Markdown file provides detailed, step-by-step instructions for installing the GCC compiler on the three major operating systems.

If you'd like to see how to install GCC on Mac using the Homebrew method specifically, [this video might be helpful](https://www.youtube.com/watch?v=NYC6W-DsFcU).