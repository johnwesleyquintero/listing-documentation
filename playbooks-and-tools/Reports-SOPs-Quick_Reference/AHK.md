### AHK

Humanized Farming Assistant

```
#MaxThreadsPerHotkey 2
#SingleInstance Force
#Persistent

; =============== CONFIGURATION ===============
minDelay := 8000    ; 8 seconds  (minimum between clicks)
maxDelay := 12000   ; 12 seconds (maximum between clicks)

; Optional: Add rare "micro-pauses" to simulate distraction
enableMicroPauses := true  ; Set to false if you don't want this
; ============================================

Pause, On
Loop
{
    Click

    ; Main random delay (8–12 seconds)
    Random, randSleep, %minDelay%, %maxDelay%
    Sleep %randSleep%

    ; --- Optional: Occasional longer pause (every ~8–15 clicks) ---
    if (enableMicroPauses)
    {
        Random, chance, 1, 12  ; ~1 in 12 chance
        if (chance = 1)
        {
            Random, longPause, 20000, 45000  ; 20–45 second break
            Sleep %longPause%
        }
    }
}

; Toggle auto-clicking
F8::Pause, Toggle

; Emergency exit
F12::ExitApp

; Show current status (optional)
F9::
    if (A_IsPaused)
        ToolTip, Status: PAUSED, , , 2
    else
        ToolTip, Status: CLICKING (8–12s + breaks), , , 2
    SetTimer, RemoveToolTip, 1500
return

RemoveToolTip:
    SetTimer, RemoveToolTip, Off
    ToolTip
return
```
