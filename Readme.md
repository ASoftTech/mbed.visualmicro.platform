# Readme

## Overview

This is an experiment in trying to get visual Micro Working with the mbed-cli tool
For install / useage of the mbed-cli tool I've put some details up on my blog

  * http://grbd.github.io/posts/2016/11/06/using-the-mbed-cli/

## Setup

  * Install / Setup the mbed-cli tool and depends
  * Place the "Micro Platforms" directory into "Documents\Visual Micro" or whichever directory you've selected
    within visual studio under Tools -> Options -> Visual Micro

## Status

I can get the Mbed OS listed in the Visual Micro Platforms list, and the boards list for the items I've created. <br>
But trying to do a build leads to:

```
Compiling debug version of 'BlinkyTest1' for 'Mbed Generic'
System.ArgumentException: The path is not of a legal form.
   at System.IO.Path.LegacyNormalizePath(String path, Boolean fullCheck, Int32 maxPathLength, Boolean expandShortPaths)
   at System.IO.Path.NormalizePath(String path, Boolean fullCheck, Int32 maxPathLength, Boolean expandShortPaths)
   at System.IO.Path.GetFullPathInternal(String path)
   at System.IO.DirectoryInfo.Init(String path, Boolean checkHost)
   at System.IO.DirectoryInfo..ctor(String path)
   at Visual.Micro.MiroAppAPI.SketchCompiler.CreateFileTimeListXml(String fileType, String sPath, String outputPath)
   at Visual.Micro.MiroAppAPI.SketchCompilerArduino._compile(SketchBuilder lsketch, String primaryClassName, Boolean verbose, Boolean isDebug)
   at Visual.Micro.MiroAppAPI.SketchCompilerArduino.compile(SketchBuilder lsketch, String primaryClassName, Boolean verbose, Boolean isDebug)
   at Visual.Micro.Visual.Studio.Arduino.AddInApp._CompileDo(Project oProject, Boolean IsDebugStartCommand, Boolean isRebuild, Boolean UseGdbIfAvailable)
   at Visual.Micro.Visual.Studio.Arduino.AddInApp.CompileDo(Project oProject, Boolean IsDebugStartCommand, Boolean isRebuild, Boolean UseGdbIfAvailable)
   at Visual.Micro.Visual.Studio.Arduino.AddInApp.Compile(Project oProject, Boolean IsDebugStartCommand, Boolean IsRebuild, Boolean UseGdbIfAvailable)
```

Associated forum thread

  * http://www.visualmicro.com/forums/YaBB.pl?num=1478473145/0#5
