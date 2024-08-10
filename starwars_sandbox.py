import math
from cmu_graphics import *
import time
from pygame import mixer
mixer.init()

app.background = "grey" #rgb(200, 200, 200)

app.overheat = False
app.coolingFail = False
app.overheatSteps = 0
app.shootSteps = 0

backHeatLine = Line(150, 20, 250, 20)
heatLine = Line(150, 20, 150, 20, fill = "white")
heatLine.white = 255
blueHeatZone = Line(200, 20, 220, 20, fill = "blue", visible = False)

heatCountDown = Line(250, 10, 250, 30, fill = "white", arrowStart=False, arrowEnd=False, visible = False)

character = Image(r"image/image-fotor-bg-remover-2024041413832 (1).png", 200, 200)

muzzle_flash = Circle(200, 200, 5, opacity=0, fill = rgb(255,255,255))
muzzle_flash.value = 255

e5c_image = Image(r"image/E-5C.png", 0, 0, visible = False)
e5c_1 = mixer.Sound(r"sound/Blasters/E-5C_02.wav")
e5c_2 = mixer.Sound(r"sound/Blasters/E-5C_03.wav")
e5c_3 = mixer.Sound(r"sound/Blasters/E-5C_04.wav")
e5c_4 = mixer.Sound(r"sound/Blasters/E-5C_05.wav")
e5c_5 = mixer.Sound(r"sound/Blasters/E-5C_06.wav")
e5c_6 = mixer.Sound(r"sound/Blasters/E-5C_07.wav")
e5c_7 = mixer.Sound(r"sound/Blasters/E-5C_08.wav")
e5c_Sounds = [e5c_1, e5c_2, e5c_3, e5c_4, e5c_5, e5c_6, e5c_7]

rg4d_image = Image(r"image/RG-4D.png", 0, 0, visible = False)
rg4d_12 = mixer.Sound(r"sound/Blasters/RG-4D_12.wav")
rg4d_11 = mixer.Sound(r"sound/Blasters/RG-4D_11.wav")
rg4d_10 = mixer.Sound(r"sound/Blasters/RG-4D_10.wav")
rg4d_9 = mixer.Sound(r"sound/Blasters/RG-4D_09.wav")
rg4d_8 = mixer.Sound(r"sound/Blasters/RG-4D_08.wav")
rg4d_7 = mixer.Sound(r"sound/Blasters/RG-4D_07.wav")
rg4d_6 = mixer.Sound(r"sound/Blasters/RG-4D_06.wav")
rg4d_5 = mixer.Sound(r"sound/Blasters/RG-4D_05.wav")
rg4d_4 = mixer.Sound(r"sound/Blasters/RG-4D_04.wav")
rg4d_3 = mixer.Sound(r"sound/Blasters/RG-4D_03.wav")
rg4d_2 = mixer.Sound(r"sound/Blasters/RG-4D_02.wav")
rg4d_1 = mixer.Sound(r"sound/Blasters/RG-4D_01.wav")
rg4d_Sounds = [rg4d_12, rg4d_11, rg4d_10, rg4d_9, rg4d_8, rg4d_7, rg4d_6, rg4d_5, rg4d_4, rg4d_3, rg4d_2, rg4d_1]

dc15_image = Image(r"image/DC-15.png", 0, 0, visible = False)
dc15a_Image = Image(r"image/DC-15_blaster_rifle_-_SW_Card_Trader-fotor-bg-remover-202404192044_20.png", 0, 0, visible = False)
dc15_1 = mixer.Sound(r"sound/Blasters/DC15_01.wav")
dc15_2 = mixer.Sound(r"sound/Blasters/DC15_02.wav")
dc15_3 = mixer.Sound(r"sound/Blasters/DC15_03.wav")
dc15_4 = mixer.Sound(r"sound/Blasters/DC15_04.wav")
dc15_5 = mixer.Sound(r"sound/Blasters/DC15_05.wav")
dc15_6 = mixer.Sound(r"sound/Blasters/DC15_06.wav")
dc15_7 = mixer.Sound(r"sound/Blasters/DC15_07.wav")
dc15_8 = mixer.Sound(r"sound/Blasters/DC15_08.wav")
dc15_Sounds = [dc15_1, dc15_2, dc15_3, dc15_4, dc15_5, dc15_6, dc15_7, dc15_8]

overheat1 = mixer.Sound(r"sound/UI/Overheat_Overheated_01.wav")
overheat2 = mixer.Sound(r"sound/UI/Overheat_Overheated_02.wav")
overheat3 = mixer.Sound(r"sound/UI/Overheat_Overheated_03.wav")
overheat4 = mixer.Sound(r"sound/UI/Overheat_Overheated_04.wav")
overheat_Sounds = [overheat1, overheat2, overheat3, overheat4]

coolingFail1 = mixer.Sound(r"sound/UI/OverheatActiveCoolingFail_01.wav")
coolingFail2 = mixer.Sound(r"sound/UI/OverheatActiveCoolingFail_02.wav")
coolingFail3 = mixer.Sound(r"sound/UI/OverheatActiveCoolingFail_03.wav")
coolingFail4 = mixer.Sound(r"sound/UI/OverheatActiveCoolingFail_04.wav")
coolingFail5 = mixer.Sound(r"sound/UI/OverheatActiveCoolingFail_05.wav")
coolingFail6 = mixer.Sound(r"sound/UI/OverheatActiveCoolingFail_06.wav")
coolingFail7 = mixer.Sound(r"sound/UI/OverheatActiveCoolingFail_07.wav")
coolingFail_Sounds = [coolingFail1, coolingFail2, coolingFail3, coolingFail4, coolingFail5, coolingFail6, coolingFail7]

activeCooling1 = mixer.Sound(r"sound/UI/OverheatActiveCoolingSuccess_01.wav")
activeCooling2 = mixer.Sound(r"sound/UI/OverheatActiveCoolingSuccess_02.wav")
activeCooling3 = mixer.Sound(r"sound/UI/OverheatActiveCoolingSuccess_03.wav")
activeCooling4 = mixer.Sound(r"sound/UI/OverheatActiveCoolingSuccess_04.wav")
activeCooling_Sounds = [activeCooling1, activeCooling2, activeCooling3, activeCooling4]

overheatReset1 = mixer.Sound(r"sound/UI/Overheat_Reset_01.wav")
overheatReset2 = mixer.Sound(r"sound/UI/Overheat_Reset_02.wav")
overheatReset3 = mixer.Sound(r"sound/UI/Overheat_Reset_03.wav")
overheatReset4 = mixer.Sound(r"sound/UI/Overheat_Reset_04.wav")
overheatResetSounds = [overheatReset1, overheatReset2, overheatReset3, overheatReset4]

dc17_image = Image(r"image/DC-17.png", 0, 0, visible = False)
dc17_1 = mixer.Sound(r"sound/Blasters/DC17_01.wav")
dc17_2 = mixer.Sound(r"sound/Blasters/DC17_02.wav")
dc17_3 = mixer.Sound(r"sound/Blasters/DC17_03.wav")
dc17_4 = mixer.Sound(r"sound/Blasters/DC17_04.wav")
dc17_5 = mixer.Sound(r"sound/Blasters/DC17_05.wav")
dc17_6 = mixer.Sound(r"sound/Blasters/DC17_06.wav")
dc17_7 = mixer.Sound(r"sound/Blasters/DC17_07.wav")
dc17_8 = mixer.Sound(r"sound/Blasters/DC17_08.wav")
dc17_Sounds = [dc17_1, dc17_2, dc17_3, dc17_4, dc17_5, dc17_6, dc17_7, dc17_8]

z6_image = Image(r"image/Z6.png", 0, 0, visible = False)
z6_shoot_8 = mixer.Sound(r"sound/Blasters/Z6RotaryBlaster_08.wav")
z6_shoot_7 = mixer.Sound(r"sound/Blasters/Z6RotaryBlaster_07.wav")
z6_shoot_6 = mixer.Sound(r"sound/Blasters/Z6RotaryBlaster_06.wav")
z6_shoot_5 = mixer.Sound(r"sound/Blasters/Z6RotaryBlaster_05.wav")
z6_shoot_4 = mixer.Sound(r"sound/Blasters/Z6RotaryBlaster_04.wav")
z6_shoot_3 = mixer.Sound(r"sound/Blasters/Z6RotaryBlaster_03.wav")
z6_shoot_2 = mixer.Sound(r"sound/Blasters/Z6RotaryBlaster_02.wav")
z6_shoot_1 = mixer.Sound(r"sound/Blasters/Z6RotaryBlaster_01.wav")
z6_shoot_0 = mixer.Sound(r"sound/Blasters/Z6RotaryBlaster_00.wav")
z6_shoot_Sounds = [z6_shoot_8, z6_shoot_7, z6_shoot_6, z6_shoot_5, z6_shoot_4, z6_shoot_3, z6_shoot_2, z6_shoot_1, z6_shoot_0]

valken38x_image = Image(r"image/Valken-38x.png", 0, 0, visible = False)
valken38x_5 = mixer.Sound(r"sound/Blasters/Valken-38X_05.wav")
valken38x_4 = mixer.Sound(r"sound/Blasters/Valken-38X_04.wav")
valken38x_3 = mixer.Sound(r"sound/Blasters/Valken-38X_03.wav")
valken38x_2 = mixer.Sound(r"sound/Blasters/Valken-38X_02.wav")
valken38x_1 = mixer.Sound(r"sound/Blasters/Valken-38X_01.wav")
valken38x_Sounds = [valken38x_5, valken38x_4, valken38x_3, valken38x_2, valken38x_1]

t21_image = Image(r"image/T-21.png", 0, 0, visible = False)
t21_6 = mixer.Sound(r"sound/Blasters/T21_06.wav")
t21_5 = mixer.Sound(r"sound/Blasters/T21_05.wav")
t21_4 = mixer.Sound(r"sound/Blasters/T21_04.wav")
t21_3 = mixer.Sound(r"sound/Blasters/T21_03.wav")
t21_2 = mixer.Sound(r"sound/Blasters/T21_02.wav")
t21_1 = mixer.Sound(r"sound/Blasters/T21_01.wav")
t21_Sounds = [t21_6, t21_5, t21_4, t21_3, t21_2, t21_1]

e5s_image = Image(r"image/E-5S.png", 0, 0, visible = False)
e5s_5 = mixer.Sound(r"sound/Blasters/E5S_05.wav")
e5s_4 = mixer.Sound(r"sound/Blasters/E5S_04.wav")
e5s_3 = mixer.Sound(r"sound/Blasters/E5S_03.wav")
e5s_2 = mixer.Sound(r"sound/Blasters/E5S_02.wav")
e5s_1 = mixer.Sound(r"sound/Blasters/E5S_01.wav")
e5s_Sounds = [e5s_5, e5s_4, e5s_3, e5s_2, e5s_1]

e5_image = Image(r"image/E-5.png", 0, 0, visible = False)
e5_6 = mixer.Sound(r"sound/Blasters/E5_06.wav")
e5_5 = mixer.Sound(r"sound/Blasters/E5_05.wav")
e5_4 = mixer.Sound(r"sound/Blasters/E5_04.wav")
e5_3 = mixer.Sound(r"sound/Blasters/E5_03.wav")
e5_2 = mixer.Sound(r"sound/Blasters/E5_02.wav")
e5_1 = mixer.Sound(r"sound/Blasters/E5_01.wav")
e5_Sounds = [e5_6, e5_5, e5_4, e5_3, e5_2, e5_1]

e5bx_5 = mixer.Sound(r"sound/Blasters/E5_BX_05.wav")
e5bx_4 = mixer.Sound(r"sound/Blasters/E5_BX_04.wav")
e5bx_3 = mixer.Sound(r"sound/Blasters/E5_BX_03.wav")
e5bx_2 = mixer.Sound(r"sound/Blasters/E5_BX_02.wav")
e5bx_1 = mixer.Sound(r"sound/Blasters/E5_BX_01.wav")
e5bx_Sounds = [e5bx_5, e5bx_4, e5bx_3, e5bx_2, e5bx_1]

droideka_shoot_6 = mixer.Sound(r"sound/Blasters/DroidekaTwinBlaster_06.wav")
droideka_shoot_5 = mixer.Sound(r"sound/Blasters/DroidekaTwinBlaster_05.wav")
droideka_shoot_4 = mixer.Sound(r"sound/Blasters/DroidekaTwinBlaster_04.wav")
droideka_shoot_3 = mixer.Sound(r"sound/Blasters/DroidekaTwinBlaster_03.wav")
droideka_shoot_2 = mixer.Sound(r"sound/Blasters/DroidekaTwinBlaster_02.wav")
droideka_shoot_1 = mixer.Sound(r"sound/Blasters/DroidekaTwinBlaster_01.wav")
droideka_shoot_Sounds = [droideka_shoot_6, droideka_shoot_5, droideka_shoot_4, droideka_shoot_3, droideka_shoot_2, droideka_shoot_1]

dc17m_image = Image(r"image/DC-17M.png", 0, 0, visible = False)
dc17m_9 = mixer.Sound(r"sound/Blasters/DC17M_09.wav")
dc17m_8 = mixer.Sound(r"sound/Blasters/DC17M_08.wav")
dc17m_7 = mixer.Sound(r"sound/Blasters/DC17M_07.wav")
dc17m_6 = mixer.Sound(r"sound/Blasters/DC17M_06.wav")
dc17m_5 = mixer.Sound(r"sound/Blasters/DC17M_05.wav")
dc17m_4 = mixer.Sound(r"sound/Blasters/DC17M_04.wav")
dc17m_3 = mixer.Sound(r"sound/Blasters/DC17M_03.wav")
dc17m_2 = mixer.Sound(r"sound/Blasters/DC17M_02.wav")
dc17m_1 = mixer.Sound(r"sound/Blasters/DC17M_01.wav")
dc17m_Sounds = [dc17m_9, dc17m_8, dc17m_7, dc17m_6, dc17m_5, dc17m_4, dc17m_3, dc17m_2, dc17m_1]

b2_laser_5 = mixer.Sound(r"sound/Blasters/E5-B2_05.wav")
b2_laser_4 = mixer.Sound(r"sound/Blasters/E5-B2_04.wav")
b2_laser_3 = mixer.Sound(r"sound/Blasters/E5-B2_03.wav")
b2_laser_2 = mixer.Sound(r"sound/Blasters/E5-B2_02.wav")
b2_laser_1 = mixer.Sound(r"sound/Blasters/E5-B2_01.wav")
b2_laser_Sounds = [b2_laser_5, b2_laser_4, b2_laser_3, b2_laser_2, b2_laser_1]

z6_start_4 = mixer.Sound(r"sound/Blasters/Z6RotaryBlaster_Start_Short_04.wav")
z6_start_3 = mixer.Sound(r"sound/Blasters/Z6RotaryBlaster_Start_Short_03.wav")
z6_start_2 = mixer.Sound(r"sound/Blasters/Z6RotaryBlaster_Start_Short_02.wav")
z6_start_1 = mixer.Sound(r"sound/Blasters/Z6RotaryBlaster_Start_Short_01.wav")
z6_start_Sounds = [z6_start_4, z6_start_3, z6_start_2, z6_start_1]

z6_loop_Sound = mixer.Sound(r"sound/Blasters/Z6RotaryBlaster_Loop_01.wav")

z6_stop_Sound = mixer.Sound(r"sound/Blasters/Z6RotaryBlaster_Stop_01.wav")

lightsaber_start_6 = mixer.Sound(r"sound/Lightsaber/LightSaber_Start_LightSide_Blue_Classic_06.wav")
lightsaber_start_5 = mixer.Sound(r"sound/Lightsaber/LightSaber_Start_LightSide_Blue_Classic_05.wav")
lightsaber_start_4 = mixer.Sound(r"sound/Lightsaber/LightSaber_Start_LightSide_Blue_Classic_04.wav")
lightsaber_start_3 = mixer.Sound(r"sound/Lightsaber/LightSaber_Start_LightSide_Blue_Classic_03.wav")
lightsaber_start_2 = mixer.Sound(r"sound/Lightsaber/LightSaber_Start_LightSide_Blue_Classic_02.wav")
lightsaber_start_1 = mixer.Sound(r"sound/Lightsaber/LightSaber_Start_LightSide_Blue_Classic_01.wav")
lightsaber_start_Sounds = [lightsaber_start_6, lightsaber_start_5, lightsaber_start_4, lightsaber_start_3, lightsaber_start_2, lightsaber_start_1]

lightsaber_idle_Sound = mixer.Sound(r"sound/Lightsaber/LightSaber_Idle_LightSide_Blue_01.wav")

lightsaber_swing_15 = mixer.Sound(r"sound/Lightsaber/LightSaber_Swing_Fast_015.wav")
lightsaber_swing_14 = mixer.Sound(r"sound/Lightsaber/LightSaber_Swing_Fast_014.wav")
lightsaber_swing_13 = mixer.Sound(r"sound/Lightsaber/LightSaber_Swing_Fast_013.wav")
lightsaber_swing_12 = mixer.Sound(r"sound/Lightsaber/LightSaber_Swing_Fast_012.wav")
lightsaber_swing_11 = mixer.Sound(r"sound/Lightsaber/LightSaber_Swing_Fast_011.wav")
lightsaber_swing_10 = mixer.Sound(r"sound/Lightsaber/LightSaber_Swing_Fast_010.wav")
lightsaber_swing_9 = mixer.Sound(r"sound/Lightsaber/LightSaber_Swing_Fast_09.wav")
lightsaber_swing_8 = mixer.Sound(r"sound/Lightsaber/LightSaber_Swing_Fast_08.wav")
lightsaber_swing_7 = mixer.Sound(r"sound/Lightsaber/LightSaber_Swing_Fast_07.wav")
lightsaber_swing_6 = mixer.Sound(r"sound/Lightsaber/LightSaber_Swing_Fast_06.wav")
lightsaber_swing_5 = mixer.Sound(r"sound/Lightsaber/LightSaber_Swing_Fast_05.wav")
lightsaber_swing_4 = mixer.Sound(r"sound/Lightsaber/LightSaber_Swing_Fast_04.wav")
lightsaber_swing_3 = mixer.Sound(r"sound/Lightsaber/LightSaber_Swing_Fast_03.wav")
lightsaber_swing_2 = mixer.Sound(r"sound/Lightsaber/LightSaber_Swing_Fast_02.wav")
lightsaber_swing_1 = mixer.Sound(r"sound/Lightsaber/LightSaber_Swing_Fast_01.wav")
lightsaber_swing_Sounds = [lightsaber_swing_15, lightsaber_swing_14, lightsaber_swing_13, lightsaber_swing_12, lightsaber_swing_11, lightsaber_swing_10, lightsaber_swing_9, lightsaber_swing_8, lightsaber_swing_7, lightsaber_swing_6, lightsaber_swing_5, lightsaber_swing_4, lightsaber_swing_3, lightsaber_swing_2, lightsaber_swing_1]

lightsaber_stop_5 = mixer.Sound(r"sound/Lightsaber/LightSaber_Stop_LightSide_Blue_05.wav")
lightsaber_stop_4 = mixer.Sound(r"sound/Lightsaber/LightSaber_Stop_LightSide_Blue_04.wav")
lightsaber_stop_3 = mixer.Sound(r"sound/Lightsaber/LightSaber_Stop_LightSide_Blue_03.wav")
lightsaber_stop_2 = mixer.Sound(r"sound/Lightsaber/LightSaber_Stop_LightSide_Blue_02.wav")
lightsaber_stop_1 = mixer.Sound(r"sound/Lightsaber/LightSaber_Stop_LightSide_Blue_01.wav")
lightsaber_stop_Sounds = [lightsaber_stop_5, lightsaber_stop_4, lightsaber_stop_3, lightsaber_stop_2, lightsaber_stop_1]

lightsaber_spin_Sound = mixer.Sound(r"sound/Lightsaber/LightSaber_SaberThrow_Projectile_01.wav")

lightsaber_impact_1 = mixer.Sound(r"sound/Lightsaber/Impact/Short/LightSaber_Impacts_Generic_01.wav")
lightsaber_impact_2 = mixer.Sound(r"sound/Lightsaber/Impact/Short/LightSaber_Impacts_Generic_02.wav")
lightsaber_impact_3 = mixer.Sound(r"sound/Lightsaber/Impact/Short/LightSaber_Impacts_Generic_03.wav")
lightsaber_impact_4 = mixer.Sound(r"sound/Lightsaber/Impact/Short/LightSaber_Impacts_Generic_04.wav")
lightsaber_impact_5 = mixer.Sound(r"sound/Lightsaber/Impact/Short/LightSaber_Impacts_Generic_05.wav")
lightsaber_impact_6 = mixer.Sound(r"sound/Lightsaber/Impact/Short/LightSaber_Impacts_Generic_06.wav")
lightsaber_impact_7 = mixer.Sound(r"sound/Lightsaber/Impact/Short/LightSaber_Impacts_Generic_07.wav")
lightsaber_impact_8 = mixer.Sound(r"sound/Lightsaber/Impact/Short/LightSaber_Impacts_Generic_08.wav")
lightsaber_impact_9 = mixer.Sound(r"sound/Lightsaber/Impact/Short/LightSaber_Impacts_Generic_09.wav")
lightsaber_impact_10 = mixer.Sound(r"sound/Lightsaber/Impact/Short/LightSaber_Impacts_Generic_010.wav")
lightsaber_impact_11 = mixer.Sound(r"sound/Lightsaber/Impact/Short/LightSaber_Impacts_Generic_011.wav")
lightsaber_impact_12 = mixer.Sound(r"sound/Lightsaber/Impact/Short/LightSaber_Impacts_Generic_012.wav")
lightsaber_impact_13 = mixer.Sound(r"sound/Lightsaber/Impact/Short/LightSaber_Impacts_Generic_013.wav")
lightsaber_impact_14 = mixer.Sound(r"sound/Lightsaber/Impact/Short/LightSaber_Impacts_Generic_014.wav")
lightsaber_impact_15 = mixer.Sound(r"sound/Lightsaber/Impact/Short/LightSaber_Impacts_Generic_015.wav")
lightsaber_impact_16 = mixer.Sound(r"sound/Lightsaber/Impact/Short/LightSaber_Impacts_Generic_016.wav")
lightsaber_impact_17 = mixer.Sound(r"sound/Lightsaber/Impact/Short/LightSaber_Impacts_Generic_017.wav")
lightsaber_impact_18 = mixer.Sound(r"sound/Lightsaber/Impact/Short/LightSaber_Impacts_Generic_018.wav")
lightsaber_impact_19 = mixer.Sound(r"sound/Lightsaber/Impact/Short/LightSaber_Impacts_Generic_019.wav")
lightsaber_impact_20 = mixer.Sound(r"sound/Lightsaber/Impact/Short/LightSaber_Impacts_Generic_020.wav")
lightsaber_impact_21 = mixer.Sound(r"sound/Lightsaber/Impact/Short/LightSaber_Impacts_Generic_021.wav")
lightsaber_impact_22 = mixer.Sound(r"sound/Lightsaber/Impact/Short/LightSaber_Impacts_Generic_022.wav")
lightsaber_impact_Sounds = [lightsaber_impact_1, lightsaber_impact_2, lightsaber_impact_3, lightsaber_impact_4, lightsaber_impact_5, lightsaber_impact_6, lightsaber_impact_7, lightsaber_impact_8, lightsaber_impact_9, lightsaber_impact_10, lightsaber_impact_11, lightsaber_impact_12, lightsaber_impact_13, lightsaber_impact_14, lightsaber_impact_15, lightsaber_impact_16, lightsaber_impact_17, lightsaber_impact_18, lightsaber_impact_19, lightsaber_impact_20, lightsaber_impact_21, lightsaber_impact_22]

onBlasterHit_51 = mixer.Sound(r"sound/UI/UX_Shared_OnBlasterHit_VAR_51.wav")
onBlasterHit_52 = mixer.Sound(r"sound/UI/UX_Shared_OnBlasterHit_VAR_52.wav")
onBlasterHit_53 = mixer.Sound(r"sound/UI/UX_Shared_OnBlasterHit_VAR_53.wav")
onBlasterHit_54 = mixer.Sound(r"sound/UI/UX_Shared_OnBlasterHit_VAR_54.wav")
onBlasterHit_55 = mixer.Sound(r"sound/UI/UX_Shared_OnBlasterHit_VAR_55.wav")
onBlasterHit_56 = mixer.Sound(r"sound/UI/UX_Shared_OnBlasterHit_VAR_56.wav")
onBlasterHit_57 = mixer.Sound(r"sound/UI/UX_Shared_OnBlasterHit_VAR_57.wav")
onBlasterHit_58 = mixer.Sound(r"sound/UI/UX_Shared_OnBlasterHit_VAR_58.wav")
onBlasterHit_Sounds = [onBlasterHit_51, onBlasterHit_52, onBlasterHit_53, onBlasterHit_54, onBlasterHit_55, onBlasterHit_56, onBlasterHit_57, onBlasterHit_58]


ib94_image = Image(r"image/IB-94.png", 0, 0, visible = False)
ib94_1 = mixer.Sound(r"sound/Blasters/IB-94 blaster1.mp3")
ib94_2 = mixer.Sound(r"sound/Blasters/IB-94 blaster2.mp3")
ib94_3 = mixer.Sound(r"sound/Blasters/IB-94 blaster3.mp3")
ib94_4 = mixer.Sound(r"sound/Blasters/IB-94 blaster4.mp3")
ib94_5 = mixer.Sound(r"sound/Blasters/IB-94 blaster5.mp3")
ib94_6 = mixer.Sound(r"sound/Blasters/IB-94 blaster6.mp3")
ib94_7 = mixer.Sound(r"sound/Blasters/IB-94 blaster7.mp3")
ib94_Sounds = [ib94_1, ib94_2, ib94_3, ib94_4, ib94_5, ib94_6, ib94_7]


####################################################### Weapon Data: #####################################################################################
# Property:     [gun name,     color,   sound list,          random, heatX2,    muzzle flash,  RPM,  speed, damage, heatRed, image,     recoil, offset, length]
# Index number: [0              1           2                   3       4           5           6       7     8     9           10          11  12  13]
dc15 =          ["DC-15",       "blue",  dc15_Sounds,            10,   2.5,      rgb(0, 0, 255), 55,     3,   34,    12.75,  dc15_image,     5, 5,  25]
dc15a =         ["DC-15A",     "blue",  dc15_Sounds,            8,    2.5,      rgb(0, 0, 255), 35,     3,   20,    8,      dc15a_Image,     5, 10, 50]
dc17 =          ["DC-17",      "blue",  dc17_Sounds,            15,   5,        rgb(0, 0, 255), 125,    3,   25,    15,     dc17_image,      5, 0,  15]
valken38x =     ["Valken-38X", "blue",  valken38x_Sounds,       100,  10,       rgb(0, 0, 255), 200,    7,   55,    25,     valken38x_image, 5, 10, 50]
dc17m =         ["DC-17M",     "blue",  dc17m_Sounds,           10,   2.5,      rgb(0, 0, 255), 35,     4,   34,    12.75,  dc17m_image,     5, 5,  25]
z6 =            ["Z6",         "blue",  z6_shoot_Sounds,        5,    0.875,    rgb(0, 0, 255), 20,     2.5, 20,    4,      z6_image,        5, 8,  50]
t21 =           ["T-21",       "blue",  t21_Sounds,             50,   2.5,      rgb(0, 0, 255), 105,    5,   34,    15,     t21_image,       5, 5,  50]
e5 =            ["E-5",         "red",   e5_Sounds,              10,   2.5,      rgb(0, 0, 255), 55,     3,   34,    12.75,  e5_image,       5, 5,  25]
e5c =           ["E-5C",       "red",   e5c_Sounds,             8,    2.5,      rgb(0, 0, 255), 35,     3,   20,    8,      e5c_image,       5, 8,  50]
rg4d =          ["RG-4D",      "red",   rg4d_Sounds,            15,   5,        rgb(0, 0, 255), 80,     3,   25,    15,     rg4d_image,      5, 0,  15]
e5s =           ["E-5S",       "red",   e5s_Sounds,             100,  10,       rgb(0, 0, 255), 200,    7,   55,    25,     e5s_image,       5, 10, 50]
b2laser =       ["B2",         "red",   b2_laser_Sounds,        10,   2.5,      rgb(0, 0, 255), 35,     4,   34,    12.75,  None,            5, 0,  25]
droidekalaser = ["Droideka",   "red",   droideka_shoot_Sounds,  5,    1.75,     rgb(0, 0, 255), 70,     4,   34,    12.75,  None,            5, 0,  25]
e5bx =          ["E-5BX",      "red",   e5bx_Sounds,            10,   2.5,      rgb(0, 0, 255), 45,     4,   34,    12.75,  e5_image,        5, 5,  25]
ib94 =          ["IB-94",      "red",   ib94_Sounds,            12,   2.5,      rgb(0, 0, 255), 80,     4,   34,    15,     ib94_image,      5, 3,  20]
#########################################################################################################################################################

# Light Saber
lightsaber = ["Light Saber", "blue", dc15_Sounds, 1, 2.5, rgb(0, 0, 255), 10000000000000000000000000000000, 100, 100, 0, None, 0, 0]
lightsaber_blade = [Line(0,0,0,0, fill = "blue", lineWidth = 5), Line(0, 0, 0, 0, fill = "white", lineWidth = 3)]
lightsaber_hilt = Line(character.centerX, character.centerY, character.centerX, character.centerY, fill = gradient("gray", "lightgrey"))
lightsaber_hilt.dx = 0
lightsaber_hilt.dy = 0
app.lightsaber_length = 0
app.lightsaberOn = False

weapons = [dc15, dc15a, dc17, valken38x, dc17m, z6, t21, e5, e5c, rg4d, e5s, b2laser, droidekalaser, e5bx, lightsaber, ib94]
weapon_images = [dc15_image, dc15a_Image, dc17_image, valken38x_image, dc17m_image, z6_image, t21_image, e5_image, e5c_image, rg4d_image, e5s_image, ib94_image]
app.weaponIndex = len(weapons) - 1

def randomSound(list):
    """
    Plays a random sound from the given list.

    Args:
        list (list): A list of Sound objects.
    """
    for sound in list: sound.stop() # Stop all sounds
    sound = list[randrange(0,len(list))]    # Pick a random sound
    sound.play()    # Play the sound

enemies = []

# Create bullet objects
offScreenBullets = []
onScreenBullets = []
for i in range(1,30):
    bullet = [Line(0,0,0,0, fill = weapons[app.weaponIndex][1], lineWidth = 5), Line(0, 0, 0, 0, fill = "white", lineWidth = 3)]
    offScreenBullets.append(bullet)

# Create enemy objects
def spawnEnemies():
    for i in range(10):
        randx = randrange(0, 400)
        randy = randrange(0, 400)
        enemy = Group(Image(r"image/b1_droid_head.png", randx, randy))# Rect(randx, randy- 20, 20, 50, visible = False, opacity = 0))
        enemy.health = 100
        enemy.has_been_hit = False
        enemies.append(enemy)

# Handle character movement
def onKeyHold(keys):
    if "w" in keys:
        character.centerY -= 1
    if "a" in keys:
        character.centerX -= 1
    if "s" in keys:
        character.centerY += 1
    if "d" in keys:
        character.centerX += 1

def switchWeapon(weapon = None):

    for image in weapon_images: # Hide all weapon images
        if image != None: image.visible = False

    if weapon == None:  # Switch to next weapon if weapon wasn't specified
        if app.weaponIndex +1 >= len(weapons):
            app.weaponIndex = 0
        else:
            app.weaponIndex += 1

    else:   # Switch to the specified weapon
        for weaponList in weapons:
            if weaponList[0] == weapon:
                app.weaponIndex = weapons.index(weaponList)
                break
            
    if weapons[app.weaponIndex][10] != None: weapons[app.weaponIndex][10].visible = True    # Make the weapon image visible
    mixer.Sound(r"sound/UI/UX_Navigation_WeaponEquip_01.wav").play()   # Play weapon change sound

    # Reset heat
    heatLine.white = 255
    heatLine.x2 = 150
    heatLine.fill = "white"
    blueHeatZone.visible = False
    heatCountDown.visible = False
    heatCountDown.centerX = 250
    randomSound(overheatResetSounds)
    app.coolingFail = False
    app.overheat = False
    app.overheatSteps = 0

def onKeyPress(key):

    if key == "space":
        switchWeapon()


# Shooting
app.z6_startup = False
app.dc17_2 = False
app.recoil = 0
app.shooting = False
app.prematureShoot = False

def shoot(x, y):
    """
    Shoot a bullet from the character's position.
    
    Parameters:
    x (int): The x-coordinate of the mouse cursor.
    y (int): The y-coordinate of the mouse cursor.

    Side Effects:
    - Adds a new bullet to the on-screen bullets list.
    - Updates the game state based on the weapon's properties.
    """
    if app.overheat == False:   # Attempt to shoot if the weapon is not overheated

        # Handle overheating
        if heatLine.x2 >= 247.5:    
            app.overheat = True
            app.overheatSteps = 0 
            heatLine.x2 = 250
            heatLine.white = 0
            randomSound(overheat_Sounds)
            # Handle Z6 stopping
            if weapons[app.weaponIndex] == z6:
                app.z6_startup_steps = 0
                z6_loop_Sound.stop()
                z6_stop_Sound.play()
        
        else:   # Shoot
            randomSound(weapons[app.weaponIndex][2])    # Play shooting sound
            app.shootSteps = 0  # Reset shoot steps
            bullet = offScreenBullets[0]    # select a bullet to shoot
            for line in bullet: line.visible = True
            bullet[0].fill = weapons[app.weaponIndex][1]    # Set bullet color
            offScreenBullets.remove(bullet) # Remove the bullet from the off-screen bullets list
            onScreenBullets.append(bullet) # Add the bullet to the on-screen bullets list
            bullet[0].dx = cursor.centerX - character.centerX # Set bullet change in x direction
            bullet[0].dy = cursor.centerY - character.centerY # Set bullet change in y direction
            length = math.sqrt(bullet[0].dx ** 2 + bullet[0].dy ** 2)   # Normalize the length of the bullet
            if length != 0:
                bullet[0].dx /= length
                bullet[0].dy /= length

            # Set bullet position    
            bullet[0].x1 = character.centerX + bullet[0].dx * weapons[app.weaponIndex][13] + weapons[app.weaponIndex][12]
            bullet[1].x1 = character.centerX + bullet[0].dx * 1.5 + bullet[0].dx * weapons[app.weaponIndex][13] + weapons[app.weaponIndex][12]
            bullet[0].y1 = character.centerY + bullet[0].dy * weapons[app.weaponIndex][13] + weapons[app.weaponIndex][12]
            bullet[1].y1 = character.centerY + bullet[0].dy * 1.5 + bullet[0].dy * weapons[app.weaponIndex][13] + weapons[app.weaponIndex][12]
            bullet[0].x2 = character.centerX + bullet[0].dx * 25.5 + bullet[0].dx * weapons[app.weaponIndex][13] + weapons[app.weaponIndex][12]
            bullet[1].x2 = character.centerX + bullet[0].dx * 25 + bullet[0].dx * weapons[app.weaponIndex][13] + weapons[app.weaponIndex][12]
            bullet[0].y2 = character.centerY + bullet[0].dy * 25.5 + bullet[0].dy * weapons[app.weaponIndex][13] + weapons[app.weaponIndex][12]
            bullet[1].y2 = character.centerY + bullet[0].dy * 25 + bullet[0].dy * weapons[app.weaponIndex][13] + weapons[app.weaponIndex][12]

            # Set muzzle flash
            muzzle_flash.centerX, muzzle_flash.centerY = character.centerX + bullet[0].dx * weapons[app.weaponIndex][13] , character.centerY + bullet[0].dy * weapons[app.weaponIndex][13] + weapons[app.weaponIndex][12]
            muzzle_flash.opacity = 75
            muzzle_flash.fill = weapons[app.weaponIndex][5]
            muzzle_flash.value = 0

            # Add a slight random offset to the bullet direction
            bullet[0].dx += randrange(-1, 2, 2) * random() / weapons[app.weaponIndex][3]
            bullet[0].dy += randrange(-1, 2, 2) * random() / weapons[app.weaponIndex][3]
            
            app.recoil = weapons[app.weaponIndex][11] # Set recoil

            heatLine.x2 += weapons[app.weaponIndex][4] # Add heat

            # Handle heat line color change
            if heatLine.x2 >= 202.5:
                if heatLine.white > 0:    heatLine.white -= weapons[app.weaponIndex][9]
                heatLine.fill = rgb(255, heatLine.white, heatLine.white)

# Mouse movement variables
cursor = Rect(1,1,1,1, opacity = 0)    
previous_x, previous_y = 0, 0
previous_time = time.time()
app.speed = 0 
app.lightsaber_swing_steps = 0
app.lightsaber_width = 9
app.lightsaber_spinning = False

def calculate_speed(x, y):
    """
    Calculate the speed of the mouse based on the difference in its position over time.
    This function takes the current position of the mouse (x, y) and the previous position (previous_x, previous_y) as input.
    It calculates the distance moved by the mouse and the time taken to move that distance.
    The function then calculates the speed of the mouse in pixels per second and returns it.

    Parameters:
    x (int): The current x-coordinate of the mouse.
    y (int): The current y-coordinate of the mouse.
    previous_x (int): The previous x-coordinate of the mouse.
    previous_y (int): The previous y-coordinate of the mouse.

    Returns:
    float: The speed of the character in pixels per second.
    """
    global previous_x, previous_y, previous_time
    # Calculate distance moved
    distance = ((x - previous_x) ** 2 + (y - previous_y) ** 2) ** 0.5

    # Calculate time taken
    current_time = time.time()
    time_difference = current_time - previous_time

    # Check for zero division error
    if time_difference == 0:
        return

    # Calculate speed
    app.speed = distance / time_difference

    # Update previous position and time
    previous_x, previous_y = x, y
    previous_time = current_time

    return app.speed

def onMouseMove(x, y):

    # Update global position variables
    cursor.centerX = x
    cursor.centerY = y
    
    # Handle lightsaber spinning
    if app.speed > 2000 and app.lightsaberOn == True and app.lightsaber_spinning == False and app.lightsaber_swing_steps > 100:
        for sound in lightsaber_swing_Sounds:
            sound.stop()
        lightsaber_spin_Sound.play(loops=100)
        app.lightsaber_spinning = True

    # Handle lightsaber swing
    elif app.speed > 400 and app.lightsaber_swing_steps > 100 and app.lightsaberOn == True:
        app.lightsaber_swing_steps = 0
        randomSound(lightsaber_swing_Sounds)

    # Handle lightsaber collision
    if app.lightsaberOn == True and app.speed > 1000:
        pass ######################

def onMousePress(x, y):

    # Toggle lightsaber
    if weapons[app.weaponIndex] == lightsaber:  
        # Turn off
        if app.lightsaberOn == True:
            app.lightsaberOn = False
            randomSound(lightsaber_stop_Sounds)
            lightsaber_idle_Sound.stop()
        
        # Turn on    
        else:
            app.lightsaberOn = True
            app.lightsaber_width = 9
            randomSound(lightsaber_start_Sounds)
            lightsaber_idle_Sound.play(loops=100, fade_ms=1000)

    # Handle shooting
    if app.steps >= weapons[app.weaponIndex][6] and app.overheat == False:    
        app.steps = 0
        app.shooting = True

    # Z6 startup
    if weapons[app.weaponIndex] == z6:
        app.z6_startup = True
        randomSound(z6_start_Sounds)
    
    # Handle overheat active cooling
    if app.overheat == True and app.coolingFail == False:

        # Handle overheat successful cooling
        if heatCountDown.hitsShape(blueHeatZone):
            heatLine.x2 = 150
            blueHeatZone.visible = False
            heatLine.fill = "white"
            heatCountDown.visible = False
            heatCountDown.centerX = 250
            heatLine.white = 255
            randomSound(activeCooling_Sounds)
            app.overheat = False
            app.overheatSteps = 0
            
        # Handle overheat unsuccessful cooling    
        else:
            app.overheatSteps = 0
            heatLine.x2 = 250
            blueHeatZone.visible = False
            heatCountDown.centerX = 250
            randomSound(coolingFail_Sounds)
            app.coolingFail = True

def onMouseRelease(x, y):
    app.shooting = False    

    # Handle Z6 stopping
    if weapons[app.weaponIndex] == z6:
        if app.z6_startup == False and app.overheat == False: z6_stop_Sound.play()
        for sound in z6_start_Sounds: sound.stop()
        app.z6_startup = False
        app.z6_startup_steps = 0
        z6_loop_Sound.stop()

def onMouseDrag(x, y):

    # Update global mouse position variables
    cursor.centerX = x
    cursor.centerY = y
    
app.stepsPerSecond = 270
app.steps = 0
app.z6_startup_steps = 0 

enemyBackgroundHealth = Line(0, 0, 0, 0)
enemyHealth = Line(0, 0, 0, 0, fill = 'white') #Line(enemy.centerX - 20, enemy.centerY - 16, enemy.centerX - 20 + enemy.health /2.5, enemy.centerY - 16, fill = "white")
def onBlasterHit(enemy, bullet):
    enemyBackgroundHealth.opacity = 100
    enemyHealth.opacity = 100
    enemy.health -= weapons[app.weaponIndex][8]
    enemy.remove(enemyBackgroundHealth)
    enemy.remove(enemyHealth)
    enemyBackgroundHealth.x1, enemyBackgroundHealth.y1, enemyBackgroundHealth.x2, enemyBackgroundHealth.y2 = enemy.centerX - 20, enemy.centerY - 20, enemy.centerX + 20, enemy.centerY - 20
    enemyHealth.x1, enemyHealth.y1, enemyHealth.x2, enemyHealth.y2 = enemy.centerX - 20, enemy.centerY - 20, enemy.centerX - 20 + enemy.health /2.5, enemy.centerY - 20
    enemy.add(enemyBackgroundHealth)
    enemy.add(enemyHealth)

    if enemy.health <= 0: 
        enemy.remove(enemyBackgroundHealth)
        enemy.remove(enemyHealth)
        enemyBackgroundHealth.opacity = 0
        enemyHealth.opacity = 0
        enemy.visible = False
        enemies.remove(enemy)
    else: 
        randomSound(onBlasterHit_Sounds) ################ add kill confirm sound
   
    enemy.has_been_hit = True
    for line in bullet: line.visible = False
    onScreenBullets.remove(bullet)
    offScreenBullets.append(bullet)
    for line in bullet: line.centerX = -50

def onStep():
    
    onScreenBullets.sort(key=lambda bullet: bullet[0].centerX)
    enemies.sort(key=lambda enemy: enemy.centerX)

    active_bullets = []
    active_enemies = []

    for bullet in onScreenBullets:
        bullet[0].has_collided = False

    for enemy in enemies:
        enemy.has_collided = False


    for bullet in onScreenBullets:
        # Remove bullets that are no longer in the active interval
        active_bullets = [active_bullet for active_bullet in active_bullets if active_bullet[0].right > bullet[0].left]

        # Check for collisions with active enemies
        for enemy in active_enemies:
            if not bullet[0].has_collided and not enemy.has_collided and bullet[0].hitsShape(enemy):
                bullet[0].has_collided = True
                enemy.has_collided = True
                onBlasterHit(enemy, bullet)

        active_bullets.append(bullet)

        # Add the current bullet to active enemies check list
        for enemy in enemies:
            if enemy.right > bullet[0].left:
                active_enemies.append(enemy)
    
    active_enemies = [active_enemy for active_enemy in active_enemies if active_enemy.right > onScreenBullets[-1][0].left]

    # Check for collisions between active enemies and remaining bullets
    for enemy in active_enemies:
        for bullet in active_bullets:
            if not bullet[0].has_collided and not enemy.has_collided and bullet[0].hitsShape(enemy):
                bullet[0].has_collided = True
                enemy.has_collided = True
                onBlasterHit(enemy, bullet)

    # Update weapon image and rotation
    if weapons[app.weaponIndex][10] != None:
        weapons[app.weaponIndex][10].centerX, weapons[app.weaponIndex][10].centerY = character.centerX, character.centerY + 15
        weapons[app.weaponIndex][10].rotateAngle = math.degrees(math.atan2(cursor.centerY - (character.centerY + 10), cursor.centerX - (character.centerX))) - app.recoil
        weapons[app.weaponIndex][10].toFront()
    
    if app.recoil > 0: app.recoil -= 0.5 # Recover from weapon recoil

    if app.steps %2 == 0:
        app.speed = 0

    # Handle lightsaber functionality 
    if weapons[app.weaponIndex] == lightsaber:

        # Handle lightsaber swing stopping
        calculate_speed(cursor.centerX, cursor.centerY)
        if app.speed < 100 and app.lightsaberOn == True:
            lightsaber_spin_Sound.stop()
            app.lightsaber_spinning = False

        # Stop lightsaber swing sounds if lightsaber is spinning
        if app.lightsaber_spinning == True:
            for sound in lightsaber_swing_Sounds:
                sound.stop()

        app.lightsaber_swing_steps += 1 # Increment steps since last swing

        # Update lightsaber direction
        lightsaber_hilt.dx = cursor.centerX - character.centerX
        lightsaber_hilt.dy = cursor.centerY - character.centerY
        length = math.sqrt(lightsaber_hilt.dx ** 2 + lightsaber_hilt.dy ** 2)
        if length != 0:
            lightsaber_hilt.dx /= length
            lightsaber_hilt.dy /= length
        
        # Update lightsaber position
        lightsaber_blade[0].x1 = character.centerX + (lightsaber_hilt.dx * 20)
        lightsaber_blade[1].x1 = character.centerX + lightsaber_hilt.dx * (app.lightsaber_length *(6.5 / 70.5)) + (lightsaber_hilt.dx * 10)
        lightsaber_blade[0].y1 = character.centerY + (lightsaber_hilt.dy * 20)
        lightsaber_blade[1].y1 = character.centerY + lightsaber_hilt.dy * (app.lightsaber_length *(6.5 / 70.5)) + (lightsaber_hilt.dy * 10)
        lightsaber_blade[0].x2 = character.centerX + lightsaber_hilt.dx * app.lightsaber_length + (lightsaber_hilt.dx * 20)
        lightsaber_blade[1].x2 = character.centerX + lightsaber_hilt.dx * (app.lightsaber_length - 0.5) + (lightsaber_hilt.dx * 20)
        lightsaber_blade[0].y2 = character.centerY + lightsaber_hilt.dy * app.lightsaber_length + (lightsaber_hilt.dy * 20)
        lightsaber_blade[1].y2 = character.centerY + lightsaber_hilt.dy * (app.lightsaber_length - 0.5) + (lightsaber_hilt.dy * 20)
        lightsaber_hilt.x1 = character.centerX
        lightsaber_hilt.y1 = character.centerY
        lightsaber_hilt.x2 = character.centerX + lightsaber_hilt.dx * 20
        lightsaber_hilt.y2 = character.centerY + lightsaber_hilt.dy * 20
        
        # Update length and width of lightsaber blade for activation and deactivation
        lightsaber_blade[0].lineWidth, lightsaber_blade[1].lineWidth  = app.lightsaber_width, app.lightsaber_width - 2.5 
        if app.lightsaberOn == True and app.lightsaber_length < 70.5: app.lightsaber_length += 1.5
        if app.lightsaberOn == True and app.lightsaber_width > 5: app.lightsaber_width -=0.04375
        elif app.lightsaberOn == False and app.lightsaber_length > 0: app.lightsaber_length -= 0.5
        
    # Handle Z6 startup    
    if app.z6_startup:
        app.z6_startup_steps += 1
        if app.z6_startup_steps > 350:
            app.z6_startup = False
            z6_loop_Sound.play(loops=100)

    # Handle DC-17 double shot
    if weapons[app.weaponIndex] == dc17 and app.shootSteps == 30 and app.dc17_2 == True: 
        app.dc17_2 = False
        shoot(cursor.centerX, cursor.centerY)

    # Handle overheat cooling
    if app.overheat == True:
        app.overheatSteps += 1
        if app.overheatSteps > 200:
            heatLine.x2 -= 0.0875
            if app.coolingFail == False: blueHeatZone.visible = True
            heatCountDown.visible = True
            heatCountDown.centerX -= 0.0875
            if heatLine.x2 <= 150:
                heatLine.white = 255
                heatLine.fill = "white"
                blueHeatZone.visible = False
                heatCountDown.visible = False
                heatCountDown.centerX = 250
                randomSound(overheatResetSounds)
                app.coolingFail = False
                app.overheat = False
                app.overheatSteps = 0
    
    # Decrease heat if idle
    else:
        if app.shootSteps > 300 and app.shootSteps % 50 == 0 and heatLine.x2 > 150:
            heatLine.x2 -= weapons[app.weaponIndex][4]
            if heatLine.x2 >= 200 and heatLine.white < 255:
                heatLine.white += 12.75
                if heatLine.white > 255: heatLine.white = 255
                heatLine.fill = rgb(255, heatLine.white, heatLine.white)


    # Handle bullet movement
    for bullet in onScreenBullets:

        # Check bullet collision with enemies
        # if app.steps % 15 == 0:
        

        # Update bullet position        
        for line in bullet:
            line.centerX += bullet[0].dx * weapons[app.weaponIndex][7] 
            line.centerY += bullet[0].dy * weapons[app.weaponIndex][7]

            # Check if bullet is off screen
            if abs(line.centerX) > 450 or abs(line.centerY) > 450:
                onScreenBullets.remove(bullet)
                offScreenBullets.append(bullet)
                break

    app.shootSteps += 1 # Increment steps since last shot

    # Handle semi auto fire
    if app.shooting == True and app.steps % weapons[app.weaponIndex][6] == 0 and app.z6_startup == False:
        if weapons[app.weaponIndex] == dc17: app.dc17_2 = True
        if weapons[app.weaponIndex] == droidekalaser: shoot(cursor.centerX, cursor.centerY)
        shoot(cursor.centerX, cursor.centerY)

    app.steps +=1 
    
    # Handle muzzle flash disappear
    if muzzle_flash.opacity > 0:
        muzzle_flash.opacity -= 2.5
    if muzzle_flash.fill != rgb(255, 255, 255):
        muzzle_flash.value += 5
        if weapons[app.weaponIndex][1] == "blue": muzzle_flash.fill = rgb(muzzle_flash.value, muzzle_flash.value, 255)
        elif weapons[app.weaponIndex][1] == "red": muzzle_flash.fill = rgb(255, muzzle_flash.value, muzzle_flash.value)


spawnEnemies()

if weapons[app.weaponIndex][10] != None: weapons[app.weaponIndex][10].visible = True

cmu_graphics.run() # type: ignore

### Weapon Image Changes:
# dc15a - fix white
# dc17 - fix white
# valken38x - flip
# dc17m - flip
# z6 - increase size
# t21 - increase size, fix white
# e5 - flip, fix white
# e5c - increase size
# e5s - flip
# ib94 - Center muzzle and fix white
