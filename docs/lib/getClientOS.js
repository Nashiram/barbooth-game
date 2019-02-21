// This script sets OSName variable as follows:
// "Windows"    for all versions of Windows
// "MacOS"      for all versions of Macintosh OS
// "Linux"      for all versions of Linux
// "UNIX"       for all other UNIX flavors 
// "Unknown OS" indicates failure to detect the OS

var OSName = "Unknown OS";
var downloadMsg = "Download  release"

if (navigator.appVersion.indexOf("Win") != -1) 
{
  OSName = "Windows";
  downloadMsg = "Download .exe";
}
if (navigator.appVersion.indexOf("Mac") != -1)
{
  OSName = "MacOS";
  downloadMsg = "Download .dmg";
} 
if (navigator.appVersion.indexOf("X11") !=- 1) 
{
  OSName = "UNIX";
  downloadMsg = "Download .tar.gz";
}
if (navigator.appVersion.indexOf("Linux") != -1) 
{
  OSName="Linux";
  downloadMsg = "Download .deb";
}

document.getElementById("download").innerHTML = downloadMsg;