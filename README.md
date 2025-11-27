# C-For-Python-Dev
A repo holding some basic implementation of c with python to make your code almost 1000x faster

# **💻 GCC Compiler Installation Guide**

The GNU Compiler Collection (GCC) is a powerful, open-source compiler that supports multiple programming languages, including C, C++, and Fortran.

Use the links below to quickly navigate to the installation instructions for your operating system:

* [Windows Installation](#windows-installation)  
  * [Method 1: Using MinGW-w64 (Recommended)](#method-1-using-mingw-w64-recommended)  
  * [Method 2: Using WSL (Windows Subsystem for Linux)](#method-2-using-wsl-windows-subsystem-for-linux)
* [macOS Installation](#macos-installation)
  * [Method 1: Installing Xcode Command Line Tools](#method-1-installing-xcode-command-line-tools)  
  * [Method 2: Using Homebrew](#method-2-using-homebrew)
* [Linux Installation](#linux-installation)  
  * [Debian/Ubuntu (apt)](#debianubuntu-apt)  
  * [Fedora/RHEL/CentOS (dnf/yum)](#fedorарhelcentos-dnfyum)  
  * [Arch Linux (pacman)](#arch-linux-pacman)

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
   ```bash
   gcc --version
   ```
   If successful, it will display the GCC version information.

### **Method 2: Using WSL (Windows Subsystem for Linux)**

If you prefer a full Linux command-line environment on Windows, WSL is an excellent choice.

1. **Enable WSL:** Open PowerShell as an Administrator and run the installation command (this also installs Ubuntu by default):  
   ```bash
   wsl --install
   ```
2. **Open WSL Terminal:** After restarting your computer (if required), open the Ubuntu/WSL terminal.  
3. **Install build-essential:** This package includes the GCC compiler, G++, and the make utility.  
   ```bash
   sudo apt update  
   sudo apt install build-essential
   ```
4. **Verify Installation:**  
   ```bash
   gcc --version
   ```

## **macOS Installation**

On macOS, the easiest way to get the core GCC and C++ compiler (clang is the Apple default, but GCC can be installed) is through the Xcode Command Line Tools or the Homebrew package manager.

### **Method 1: Installing Xcode Command Line Tools**

For most developers, installing the Command Line Tools is sufficient, as it includes the necessary compilers and development utilities.

1. **Open Terminal:** Open the Terminal application.  
2. **Run the install command:**  
   ```bash
   xcode-select --install
   ```
3. **Follow Prompts:** A software update window will appear. Click **Install** and accept the license agreement.  
4. **Verify Installation:** Once complete, running the following command will show the version of the compiler (often Clang, but compatible with most GCC flags):  
   ```bash
   gcc --version
   ```

### **Method 2: Using Homebrew**

If you need the specific GNU GCC suite (e.g., for compatibility with specific projects or Fortran), Homebrew is the preferred method.

1. **Install Homebrew (if you haven't already):**  
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
2. **Install GCC:** Use Homebrew to install the official GCC compiler. Homebrew often installs the latest stable version and names it with a version suffix (e.g., gcc-13 or g++-13).  
   ```bash
   brew install gcc
   ```
3. **Verify Installation:** Check the installed version. Note that you may need to use the version-suffixed name (gcc-13).  
   ```bash
   gcc --version  
   # or  
   gcc-13 --version 
   ```

## **Linux Installation**

On almost all modern Linux distributions, GCC is installed via the native package manager. The best practice is to install the build-essential package (or its equivalent), which includes GCC, G++, and other essential building utilities.

### **Debian/Ubuntu (apt)**

1. **Update Package Lists:**  
   ```bash
   sudo apt update
   ```
2. **Install build-essential:**  
   ```bash
   sudo apt install build-essential
   ```
3. **Verify Installation:**  
   ```bash
   gcc --version
   ```

### **Fedora/RHEL/CentOS (dnf/yum)**

These distributions use dnf (newer) or yum (older) as their package manager.

1. **Update System:**  
   ```bash
   sudo dnf update  
   # or (for older systems)  
   sudo yum update
   ```
2. **Install GCC and supporting tools:**  
   ```bash
   sudo dnf install gcc gcc-c++ make
   ```
3. **Verify Installation:**  
   ```bash
   gcc --version
   ```

### **Arch Linux (pacman)**

1. **Synchronize Package Lists:**  
   ```bash
   sudo pacman -Sy
   ```
2. **Install gcc and base-devel (for make and other tools):**  
   ```bash
   sudo pacman -S gcc base-devel
   ```
3. **Verify Installation:**  
   ```bash
   gcc --version
   ```

## **Test Your Installation**

To ensure your compiler is fully functional, create a simple hello.c file:

```c
#include <stdio.h>

int main() {  
    printf("Hello, GCC World!\n");  
    return 0;  
}
```

1. **Compile:**  
   ```bash
   gcc hello.c -o hello
   ```
2. **Run (Linux/macOS):**  
   ```bash
   ./hello
   ```
3. **Run (Windows):**  
   ```bash
   .\hello.exe
   ```

The output should be: `Hello, GCC World!`

---

This Markdown file provides detailed, step-by-step instructions for installing the GCC compiler on the three major operating systems.

If you'd like to see how to install GCC on Mac using the Homebrew method specifically, [this video might be helpful](https://www.youtube.com/watch?v=NYC6W-DsFcU).