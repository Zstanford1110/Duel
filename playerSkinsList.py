# Skin Example
# skin = {"stand_l": "",
# "stand_r": "",
# "sword_high_l": "",
# "sword_high_r": "",
# "sword_med_l": "",
# "sword_med_r": "",
# "sword_low_l": "",
# "sword_low_r": "",
# "duck_l": "",
# "duck_r": "",
# "jump_l": "",
# "jump_r": "",
# "thrust_high_l": "",
# "thrust_high_r": "",
# "thrust_med_l": "",
# "thrust_med_r": "",
# "thrust_low_l": "",
# "thrust_low_r": ""}


def getSkin(character_type):
    images_dictionary = dict()
    if character_type == "Montoya":
        images_dictionary = {
            "flag": "Resources/Images/MontoyaFlag.png",
            "sword": "Resources/Images/MontoyaSword.png",
            "run_l_1": "Resources/Images/MontoyaRun1L.png",
            "run_r_1": "Resources/Images/MontoyaRun1R.png",
            "run_l_2": "Resources/Images/MontoyaRun2L.png",
            "run_r_2": "Resources/Images/MontoyaRun2R.png",
            "run_l_3": "Resources/Images/MontoyaRun3L.png",
            "run_r_3": "Resources/Images/MontoyaRun3R.png",
            "sword_high_l": "Resources/Images/MontoyaHighL.png",
            "sword_high_r": "Resources/Images/MontoyaHighR.png",
            "sword_med_l": "Resources/Images/MontoyaMedL.png",
            "sword_med_r": "Resources/Images/MontoyaMedR.png",
            "sword_low_l": "Resources/Images/MontoyaLowL.png",
            "sword_low_r": "Resources/Images/MontoyaLowR.png",
            "duck_l": "Resources/Images/MontoyaDuckL.png",
            "duck_r": "Resources/Images/MontoyaDuckR.png",
            "thrust_high_l": "Resources/Images/MontoyaHighThrustL.png",
            "thrust_high_r": "Resources/Images/MontoyaHighThrustR.png",
            "thrust_med_l": "Resources/Images/MontoyaMedThrustL.png",
            "thrust_med_r": "Resources/Images/MontoyaMedThrustR.png",
            "thrust_low_l": "Resources/Images/MontoyaLowThrustL.png",
            "thrust_low_r": "Resources/Images/MontoyaLowThrustR.png",
            "dead_l_1": "Resources/Images/MontoyaDeath1L.png",
            "dead_r_1": "Resources/Images/MontoyaDeath1R.png",
            "dead_l_2": "Resources/Images/MontoyaDeath2L.png",
            "dead_r_2": "Resources/Images/MontoyaDeath2R.png",
            "dead_l_3": "Resources/Images/MontoyaDeath3L.png",
            "dead_r_3": "Resources/Images/MontoyaDeath3R.png",
            "ghost_run_l_1": "Resources/Images/MontoyaGhostRun1L.png",
            "ghost_run_r_1": "Resources/Images/MontoyaGhostRun1R.png",
            "ghost_run_l_2": "Resources/Images/MontoyaGhostRun2L.png",
            "ghost_run_r_2": "Resources/Images/MontoyaGhostRun2R.png",
            "ghost_run_l_3": "Resources/Images/MontoyaGhostRun3L.png",
            "ghost_run_r_3": "Resources/Images/MontoyaGhostRun3R.png",
            "ghost_sword_high_l": "Resources/Images/MontoyaGhostHighL.png",
            "ghost_sword_high_r": "Resources/Images/MontoyaGhostHighR.png",
            "ghost_sword_med_l": "Resources/Images/MontoyaGhostMedL.png",
            "ghost_sword_med_r": "Resources/Images/MontoyaGhostMedR.png",
            "ghost_sword_low_l": "Resources/Images/MontoyaGhostLowL.png",
            "ghost_sword_low_r": "Resources/Images/MontoyaGhostLowR.png",
            "ghost_duck_l": "Resources/Images/MontoyaGhostDuckL.png",
            "ghost_duck_r": "Resources/Images/MontoyaGhostDuckR.png",
            "ghost_thrust_high_l": "Resources/Images/MontoyaGhostHighThrustL.png",
            "ghost_thrust_high_r": "Resources/Images/MontoyaGhostHighThrustR.png",
            "ghost_thrust_med_l": "Resources/Images/MontoyaGhostMedThrustL.png",
            "ghost_thrust_med_r": "Resources/Images/MontoyaGhostMedThrustR.png",
            "ghost_thrust_low_l": "Resources/Images/MontoyaGhostLowThrustL.png",
            "ghost_thrust_low_r": "Resources/Images/MontoyaGhostLowThrustR.png",
            "ghost_dead_l_1": "Resources/Images/MontoyaGhostDeath1L.png",
            "ghost_dead_r_1": "Resources/Images/MontoyaGhostDeath1R.png",
            "ghost_dead_l_2": "Resources/Images/MontoyaGhostDeath2L.png",
            "ghost_dead_r_2": "Resources/Images/MontoyaGhostDeath2R.png",
            "ghost_dead_l_3": "Resources/Images/MontoyaGhostDeath3L.png",
            "ghost_dead_r_3": "Resources/Images/MontoyaGhostDeath3R.png",
            
            "run_l_nosword": "Resources/Images/MontoyaRun1L_nosword.png",
            "run_r_nosword": "Resources/Images/MontoyaRun1R_nosword.png",
            "run_l_1_nosword": "Resources/Images/MontoyaRun1L_nosword.png",
            "run_r_1_nosword": "Resources/Images/MontoyaRun1R_nosword.png",
            "run_l_2_nosword": "Resources/Images/MontoyaRun2L_nosword.png",
            "run_r_2_nosword": "Resources/Images/MontoyaRun2R_nosword.png",
            "run_l_3_nosword": "Resources/Images/MontoyaRun3L_nosword.png",
            "run_r_3_nosword": "Resources/Images/MontoyaRun3R_nosword.png",
            "sword_high_l_nosword": "Resources/Images/MontoyaHighL_nosword.png",
            "sword_high_r_nosword": "Resources/Images/MontoyaHighR_nosword.png",
            "sword_med_l_nosword": "Resources/Images/MontoyaMedL_nosword.png",
            "sword_med_r_nosword": "Resources/Images/MontoyaMedR_nosword.png",
            "sword_low_l_nosword": "Resources/Images/MontoyaLowL_nosword.png",
            "sword_low_r_nosword": "Resources/Images/MontoyaLowR_nosword.png",
            "duck_l_nosword": "Resources/Images/MontoyaDuckL_nosword.png",
            "duck_r_nosword": "Resources/Images/MontoyaDuckR_nosword.png",
            "thrust_high_l_nosword": "Resources/Images/MontoyaHighThrustL_nosword.png",
            "thrust_high_r_nosword": "Resources/Images/MontoyaHighThrustR_nosword.png",
            "thrust_med_l_nosword": "Resources/Images/MontoyaMedThrustL_nosword.png",
            "thrust_med_r_nosword": "Resources/Images/MontoyaMedThrustR_nosword.png",
            "thrust_low_l_nosword": "Resources/Images/MontoyaLowThrustL_nosword.png",
            "thrust_low_r_nosword": "Resources/Images/MontoyaLowThrustR_nosword.png",           
            "ghost_run_l_1_nosword": "Resources/Images/MontoyaGhostRun1L_nosword.png",
            "ghost_run_r_1_nosword": "Resources/Images/MontoyaGhostRun1R_nosword.png",
            "ghost_run_l_2_nosword": "Resources/Images/MontoyaGhostRun2L_nosword.png",
            "ghost_run_r_2_nosword": "Resources/Images/MontoyaGhostRun2R_nosword.png",
            "ghost_run_l_3_nosword": "Resources/Images/MontoyaGhostRun3L_nosword.png",
            "ghost_run_r_3_nosword": "Resources/Images/MontoyaGhostRun3R_nosword.png",         
            "ghost_sword_high_l_nosword": "Resources/Images/MontoyaGhostHighL_nosword.png",
            "ghost_sword_high_r_nosword": "Resources/Images/MontoyaGhostHighR_nosword.png",
            "ghost_sword_med_l_nosword": "Resources/Images/MontoyaGhostMedL_nosword.png",
            "ghost_sword_med_r_nosword": "Resources/Images/MontoyaGhostMedR_nosword.png",
            "ghost_sword_low_l_nosword": "Resources/Images/MontoyaGhostLowL_nosword.png",
            "ghost_sword_low_r_nosword": "Resources/Images/MontoyaGhostLowR_nosword.png",
            "ghost_duck_l_nosword": "Resources/Images/MontoyaGhostDuckL_nosword.png",
            "ghost_duck_r_nosword": "Resources/Images/MontoyaGhostDuckR_nosword.png",
            "ghost_thrust_high_l_nosword": "Resources/Images/MontoyaGhostHighThrustL_nosword.png",
            "ghost_thrust_high_r_nosword": "Resources/Images/MontoyaGhostHighThrustR_nosword.png",
            "ghost_thrust_med_l_nosword": "Resources/Images/MontoyaGhostMedThrustL_nosword.png",
            "ghost_thrust_med_r_nosword": "Resources/Images/MontoyaGhostMedThrustR_nosword.png",
            "ghost_thrust_low_l_nosword": "Resources/Images/MontoyaGhostLowThrustL_nosword.png",
            "ghost_thrust_low_r_nosword": "Resources/Images/MontoyaGhostLowThrustR_nosword.png"
        }
    elif character_type == "Zorro":
        images_dictionary = {
            "flag": "Resources/Images/ZorroFlag.png",
            "sword": "Resources/Images/ZorroSword.png",
            "run_l_1": "Resources/Images/ZorroRun1L.png",
            "run_r_1": "Resources/Images/ZorroRun1R.png",
            "run_l_2": "Resources/Images/ZorroRun2L.png",
            "run_r_2": "Resources/Images/ZorroRun2R.png",
            "run_l_3": "Resources/Images/ZorroRun3L.png",
            "run_r_3": "Resources/Images/ZorroRun3R.png",
            "sword_high_l": "Resources/Images/ZorroHighL.png",
            "sword_high_r": "Resources/Images/ZorroHighR.png",
            "sword_med_l": "Resources/Images/ZorroMedL.png",
            "sword_med_r": "Resources/Images/ZorroMedR.png",
            "sword_low_l": "Resources/Images/ZorroLowL.png",
            "sword_low_r": "Resources/Images/ZorroLowR.png",
            "duck_l": "Resources/Images/ZorroDuckL.png",
            "duck_r": "Resources/Images/ZorroDuckR.png",
            "thrust_high_l": "Resources/Images/ZorroHighThrustL.png",
            "thrust_high_r": "Resources/Images/ZorroHighThrustR.png",
            "thrust_med_l": "Resources/Images/ZorroMedThrustL.png",
            "thrust_med_r": "Resources/Images/ZorroMedThrustR.png",
            "thrust_low_l": "Resources/Images/ZorroLowThrustL.png",
            "thrust_low_r": "Resources/Images/ZorroLowThrustR.png",
            "dead_l_1": "Resources/Images/ZorroDeath1L.png",
            "dead_r_1": "Resources/Images/ZorroDeath1R.png",
            "dead_l_2": "Resources/Images/ZorroDeath2L.png",
            "dead_r_2": "Resources/Images/ZorroDeath2R.png",
            "dead_l_3": "Resources/Images/ZorroDeath3L.png",
            "dead_r_3": "Resources/Images/ZorroDeath3R.png",
            "ghost_run_l_1": "Resources/Images/ZorroGhostRun1L.png",
            "ghost_run_r_1": "Resources/Images/ZorroGhostRun1R.png",
            "ghost_run_l_2": "Resources/Images/ZorroGhostRun2L.png",
            "ghost_run_r_2": "Resources/Images/ZorroGhostRun2R.png",
            "ghost_run_l_3": "Resources/Images/ZorroGhostRun3L.png",
            "ghost_run_r_3": "Resources/Images/ZorroGhostRun3R.png",
            "ghost_sword_high_l": "Resources/Images/ZorroGhostHighL.png",
            "ghost_sword_high_r": "Resources/Images/ZorroGhostHighR.png",
            "ghost_sword_med_l": "Resources/Images/ZorroGhostMedL.png",
            "ghost_sword_med_r": "Resources/Images/ZorroGhostMedR.png",
            "ghost_sword_low_l": "Resources/Images/ZorroGhostLowL.png",
            "ghost_sword_low_r": "Resources/Images/ZorroGhostLowR.png",
            "ghost_duck_l": "Resources/Images/ZorroGhostDuckL.png",
            "ghost_duck_r": "Resources/Images/ZorroGhostDuckR.png",
            "ghost_thrust_high_l": "Resources/Images/ZorroGhostHighThrustL.png",
            "ghost_thrust_high_r": "Resources/Images/ZorroGhostHighThrustR.png",
            "ghost_thrust_med_l": "Resources/Images/ZorroGhostMedThrustL.png",
            "ghost_thrust_med_r": "Resources/Images/ZorroGhostMedThrustR.png",
            "ghost_thrust_low_l": "Resources/Images/ZorroGhostLowThrustL.png",
            "ghost_thrust_low_r": "Resources/Images/ZorroGhostLowThrustR.png",
            "ghost_dead_l_1": "Resources/Images/ZorroGhostDeath1L.png",
            "ghost_dead_r_1": "Resources/Images/ZorroGhostDeath1R.png",
            "ghost_dead_l_2": "Resources/Images/ZorroGhostDeath2L.png",
            "ghost_dead_r_2": "Resources/Images/ZorroGhostDeath2R.png",
            "ghost_dead_l_3": "Resources/Images/ZorroGhostDeath3L.png",
            "ghost_dead_r_3": "Resources/Images/ZorroGhostDeath3R.png",
            
            "run_l_1_nosword": "Resources/Images/ZorroRun1L_nosword.png",
            "run_r_1_nosword": "Resources/Images/ZorroRun1R_nosword.png",
            "run_l_2_nosword": "Resources/Images/ZorroRun2L_nosword.png",
            "run_r_2_nosword": "Resources/Images/ZorroRun2R_nosword.png",
            "run_l_3_nosword": "Resources/Images/ZorroRun3L_nosword.png",
            "run_r_3_nosword": "Resources/Images/ZorroRun3R_nosword.png",
            "sword_high_l_nosword": "Resources/Images/ZorroHighL_nosword.png",
            "sword_high_r_nosword": "Resources/Images/ZorroHighR_nosword.png",
            "sword_med_l_nosword": "Resources/Images/ZorroMedL_nosword.png",
            "sword_med_r_nosword": "Resources/Images/ZorroMedR_nosword.png",
            "sword_low_l_nosword": "Resources/Images/ZorroLowL_nosword.png",
            "sword_low_r_nosword": "Resources/Images/ZorroLowR_nosword.png",
            "duck_l_nosword": "Resources/Images/ZorroDuckL_nosword.png",
            "duck_r_nosword": "Resources/Images/ZorroDuckR_nosword.png",
            "thrust_high_l_nosword": "Resources/Images/ZorroHighThrustL_nosword.png",
            "thrust_high_r_nosword": "Resources/Images/ZorroHighThrustR_nosword.png",
            "thrust_med_l_nosword": "Resources/Images/ZorroMedThrustL_nosword.png",
            "thrust_med_r_nosword": "Resources/Images/ZorroMedThrustR_nosword.png",
            "thrust_low_l_nosword": "Resources/Images/ZorroLowThrustL_nosword.png",
            "thrust_low_r_nosword": "Resources/Images/ZorroLowThrustR_nosword.png",
            "ghost_run_l_1_nosword": "Resources/Images/ZorroGhostRun1L_nosword.png",
            "ghost_run_r_1_nosword": "Resources/Images/ZorroGhostRun1R_nosword.png",
            "ghost_run_l_2_nosword": "Resources/Images/ZorroGhostRun2L_nosword.png",
            "ghost_run_r_2_nosword": "Resources/Images/ZorroGhostRun2R_nosword.png",
            "ghost_run_l_3_nosword": "Resources/Images/ZorroGhostRun3L_nosword.png",
            "ghost_run_r_3_nosword": "Resources/Images/ZorroGhostRun3R_nosword.png",
            "ghost_sword_high_l_nosword": "Resources/Images/ZorroGhostHighL_nosword.png",
            "ghost_sword_high_r_nosword": "Resources/Images/ZorroGhostHighR_nosword.png",
            "ghost_sword_med_l_nosword": "Resources/Images/ZorroGhostMedL_nosword.png",
            "ghost_sword_med_r_nosword": "Resources/Images/ZorroGhostMedR_nosword.png",
            "ghost_sword_low_l_nosword": "Resources/Images/ZorroGhostLowL_nosword.png",
            "ghost_sword_low_r_nosword": "Resources/Images/ZorroGhostLowR_nosword.png",
            "ghost_duck_l_nosword": "Resources/Images/ZorroGhostDuckL_nosword.png",
            "ghost_duck_r_nosword": "Resources/Images/ZorroGhostDuckR_nosword.png",
            "ghost_thrust_high_l_nosword": "Resources/Images/ZorroGhostHighThrustL_nosword.png",
            "ghost_thrust_high_r_nosword": "Resources/Images/ZorroGhostHighThrustR_nosword.png",
            "ghost_thrust_med_l_nosword": "Resources/Images/ZorroGhostMedThrustL_nosword.png",
            "ghost_thrust_med_r_nosword": "Resources/Images/ZorroGhostMedThrustR_nosword.png",
            "ghost_thrust_low_l_nosword": "Resources/Images/ZorroGhostLowThrustL_nosword.png",
            "ghost_thrust_low_r_nosword": "Resources/Images/ZorroGhostLowThrustR_nosword.png"
        }
    elif character_type == "KingArthur":
        images_dictionary = {
            "flag": "Resources/Images/KingArthurFlag.png",
            "sword": "Resources/Images/KingArthurSword.png",
            "run_l_1": "Resources/Images/KingArthurRun1L.png",
            "run_r_1": "Resources/Images/KingArthurRun1R.png",
            "run_l_2": "Resources/Images/KingArthurRun2L.png",
            "run_r_2": "Resources/Images/KingArthurRun2R.png",
            "run_l_3": "Resources/Images/KingArthurRun3L.png",
            "run_r_3": "Resources/Images/KingArthurRun3R.png",
            "sword_high_l": "Resources/Images/KingArthurHighL.png",
            "sword_high_r": "Resources/Images/KingArthurHighR.png",
            "sword_med_l": "Resources/Images/KingArthurMedL.png",
            "sword_med_r": "Resources/Images/KingArthurMedR.png",
            "sword_low_l": "Resources/Images/KingArthurLowL.png",
            "sword_low_r": "Resources/Images/KingArthurLowR.png",
            "duck_l": "Resources/Images/KingArthurDuckL.png",
            "duck_r": "Resources/Images/KingArthurDuckR.png",
            "thrust_high_l": "Resources/Images/KingArthurHighThrustL.png",
            "thrust_high_r": "Resources/Images/KingArthurHighThrustR.png",
            "thrust_med_l": "Resources/Images/KingArthurMedThrustL.png",
            "thrust_med_r": "Resources/Images/KingArthurMedThrustR.png",
            "thrust_low_l": "Resources/Images/KingArthurLowThrustL.png",
            "thrust_low_r": "Resources/Images/KingArthurLowThrustR.png",
            "dead_l_1": "Resources/Images/KingArthurDeath1L.png",
            "dead_r_1": "Resources/Images/KingArthurDeath1R.png",
            "dead_l_2": "Resources/Images/KingArthurDeath2L.png",
            "dead_r_2": "Resources/Images/KingArthurDeath2R.png",
            "dead_l_3": "Resources/Images/KingArthurDeath3L.png",
            "dead_r_3": "Resources/Images/KingArthurDeath3R.png",
            "ghost_run_l_1": "Resources/Images/KingArthurGhostRun1L.png",
            "ghost_run_r_1": "Resources/Images/KingArthurGhostRun1R.png",
            "ghost_run_l_2": "Resources/Images/KingArthurGhostRun2L.png",
            "ghost_run_r_2": "Resources/Images/KingArthurGhostRun2R.png",
            "ghost_run_l_3": "Resources/Images/KingArthurGhostRun3L.png",
            "ghost_run_r_3": "Resources/Images/KingArthurGhostRun3R.png",
            "ghost_sword_high_l": "Resources/Images/KingArthurGhostHighL.png",
            "ghost_sword_high_r": "Resources/Images/KingArthurGhostHighR.png",
            "ghost_sword_med_l": "Resources/Images/KingArthurGhostMedL.png",
            "ghost_sword_med_r": "Resources/Images/KingArthurGhostMedR.png",
            "ghost_sword_low_l": "Resources/Images/KingArthurGhostLowL.png",
            "ghost_sword_low_r": "Resources/Images/KingArthurGhostLowR.png",
            "ghost_duck_l": "Resources/Images/KingArthurGhostDuckL.png",
            "ghost_duck_r": "Resources/Images/KingArthurGhostDuckR.png",
            "ghost_thrust_high_l": "Resources/Images/KingArthurGhostHighThrustL.png",
            "ghost_thrust_high_r": "Resources/Images/KingArthurGhostHighThrustR.png",
            "ghost_thrust_med_l": "Resources/Images/KingArthurGhostMedThrustL.png",
            "ghost_thrust_med_r": "Resources/Images/KingArthurGhostMedThrustR.png",
            "ghost_thrust_low_l": "Resources/Images/KingArthurGhostLowThrustL.png",
            "ghost_thrust_low_r": "Resources/Images/KingArthurGhostLowThrustR.png",
            "ghost_dead_l_1": "Resources/Images/KingArthurGhostDeath1L.png",
            "ghost_dead_r_1": "Resources/Images/KingArthurGhostDeath1R.png",
            "ghost_dead_l_2": "Resources/Images/KingArthurGhostDeath2L.png",
            "ghost_dead_r_2": "Resources/Images/KingArthurGhostDeath2R.png",
            "ghost_dead_l_3": "Resources/Images/KingArthurGhostDeath3L.png",
            "ghost_dead_r_3": "Resources/Images/KingArthurGhostDeath3R.png",
            
            "run_l_1_nosword": "Resources/Images/KingArthurRun1L_nosword.png",
            "run_r_1_nosword": "Resources/Images/KingArthurRun1R_nosword.png",
            "run_l_2_nosword": "Resources/Images/KingArthurRun2L_nosword.png",
            "run_r_2_nosword": "Resources/Images/KingArthurRun2R_nosword.png",
            "run_l_3_nosword": "Resources/Images/KingArthurRun3L_nosword.png",
            "run_r_3_nosword": "Resources/Images/KingArthurRun3R_nosword.png",
            "sword_high_l_nosword": "Resources/Images/KingArthurHighL_nosword.png",
            "sword_high_r_nosword": "Resources/Images/KingArthurHighR_nosword.png",
            "sword_med_l_nosword": "Resources/Images/KingArthurMedL_nosword.png",
            "sword_med_r_nosword": "Resources/Images/KingArthurMedR_nosword.png",
            "sword_low_l_nosword": "Resources/Images/KingArthurLowL_nosword.png",
            "sword_low_r_nosword": "Resources/Images/KingArthurLowR_nosword.png",
            "duck_l_nosword": "Resources/Images/KingArthurDuckL_nosword.png",
            "duck_r_nosword": "Resources/Images/KingArthurDuckR_nosword.png",
            "thrust_high_l_nosword": "Resources/Images/KingArthurHighThrustL_nosword.png",
            "thrust_high_r_nosword": "Resources/Images/KingArthurHighThrustR_nosword.png",
            "thrust_med_l_nosword": "Resources/Images/KingArthurMedThrustL_nosword.png",
            "thrust_med_r_nosword": "Resources/Images/KingArthurMedThrustR_nosword.png",
            "thrust_low_l_nosword": "Resources/Images/KingArthurLowThrustL_nosword.png",
            "thrust_low_r_nosword": "Resources/Images/KingArthurLowThrustR_nosword.png",
            "ghost_run_l_1_nosword": "Resources/Images/KingArthurGhostRun1L_nosword.png",
            "ghost_run_r_1_nosword": "Resources/Images/KingArthurGhostRun1R_nosword.png",
            "ghost_run_l_2_nosword": "Resources/Images/KingArthurGhostRun2L_nosword.png",
            "ghost_run_r_2_nosword": "Resources/Images/KingArthurGhostRun2R_nosword.png",
            "ghost_run_l_3_nosword": "Resources/Images/KingArthurGhostRun3L_nosword.png",
            "ghost_run_r_3_nosword": "Resources/Images/KingArthurGhostRun3R_nosword.png",
            "ghost_sword_high_l_nosword": "Resources/Images/KingArthurGhostHighL_nosword.png",
            "ghost_sword_high_r_nosword": "Resources/Images/KingArthurGhostHighR_nosword.png",
            "ghost_sword_med_l_nosword": "Resources/Images/KingArthurGhostMedL_nosword.png",
            "ghost_sword_med_r_nosword": "Resources/Images/KingArthurGhostMedR_nosword.png",
            "ghost_sword_low_l_nosword": "Resources/Images/KingArthurGhostLowL_nosword.png",
            "ghost_sword_low_r_nosword": "Resources/Images/KingArthurGhostLowR_nosword.png",
            "ghost_duck_l_nosword": "Resources/Images/KingArthurGhostDuckL_nosword.png",
            "ghost_duck_r_nosword": "Resources/Images/KingArthurGhostDuckR_nosword.png",
            "ghost_thrust_high_l_nosword": "Resources/Images/KingArthurGhostHighThrustL_nosword.png",
            "ghost_thrust_high_r_nosword": "Resources/Images/KingArthurGhostHighThrustR_nosword.png",
            "ghost_thrust_med_l_nosword": "Resources/Images/KingArthurGhostMedThrustL_nosword.png",
            "ghost_thrust_med_r_nosword": "Resources/Images/KingArthurGhostMedThrustR_nosword.png",
            "ghost_thrust_low_l_nosword": "Resources/Images/KingArthurGhostLowThrustL_nosword.png",
            "ghost_thrust_low_r_nosword": "Resources/Images/KingArthurGhostLowThrustR_nosword.png"
        }
    else:
        # set a default skin
        images_dictionary = {
            "flag": "Resources/Images/MontoyaFlag.png",
            "sword": "Resources/Images/MontoyaSword.png",
            "run_l_1": "Resources/Images/MontoyaRun1L.png",
            "run_r_1": "Resources/Images/MontoyaRun1R.png",
            "run_l_2": "Resources/Images/MontoyaRun2L.png",
            "run_r_2": "Resources/Images/MontoyaRun2R.png",
            "run_l_3": "Resources/Images/MontoyaRun3L.png",
            "run_r_3": "Resources/Images/MontoyaRun3R.png",
            "sword_high_l": "Resources/Images/MontoyaHighL.png",
            "sword_high_r": "Resources/Images/MontoyaHighR.png",
            "sword_med_l": "Resources/Images/MontoyaMedL.png",
            "sword_med_r": "Resources/Images/MontoyaMedR.png",
            "sword_low_l": "Resources/Images/MontoyaLowL.png",
            "sword_low_r": "Resources/Images/MontoyaLowR.png",
            "duck_l": "Resources/Images/MontoyaDuckL.png",
            "duck_r": "Resources/Images/MontoyaDuckR.png",
            "thrust_high_l": "Resources/Images/MontoyaHighThrustL.png",
            "thrust_high_r": "Resources/Images/MontoyaHighThrustR.png",
            "thrust_med_l": "Resources/Images/MontoyaMedThrustL.png",
            "thrust_med_r": "Resources/Images/MontoyaMedThrustR.png",
            "thrust_low_l": "Resources/Images/MontoyaLowThrustL.png",
            "thrust_low_r": "Resources/Images/MontoyaLowThrustR.png",
            "dead_l_1": "Resources/Images/MontoyaDeath1L.png",
            "dead_r_1": "Resources/Images/MontoyaDeath1R.png",
            "dead_l_2": "Resources/Images/MontoyaDeath2L.png",
            "dead_r_2": "Resources/Images/MontoyaDeath2R.png",
            "dead_l_3": "Resources/Images/MontoyaDeath3L.png",
            "dead_r_3": "Resources/Images/MontoyaDeath3R.png",
            "ghost_run_l_1": "Resources/Images/MontoyaGhostRun1L.png",
            "ghost_run_r_1": "Resources/Images/MontoyaGhostRun1R.png",
            "ghost_run_l_2": "Resources/Images/MontoyaGhostRun2L.png",
            "ghost_run_r_2": "Resources/Images/MontoyaGhostRun2R.png",
            "ghost_run_l_3": "Resources/Images/MontoyaGhostRun3L.png",
            "ghost_run_r_3": "Resources/Images/MontoyaGhostRun3R.png",
            "ghost_sword_high_l": "Resources/Images/MontoyaGhostHighL.png",
            "ghost_sword_high_r": "Resources/Images/MontoyaGhostHighR.png",
            "ghost_sword_med_l": "Resources/Images/MontoyaGhostMedL.png",
            "ghost_sword_med_r": "Resources/Images/MontoyaGhostMedR.png",
            "ghost_sword_low_l": "Resources/Images/MontoyaGhostLowL.png",
            "ghost_sword_low_r": "Resources/Images/MontoyaGhostLowR.png",
            "ghost_duck_l": "Resources/Images/MontoyaGhostDuckL.png",
            "ghost_duck_r": "Resources/Images/MontoyaGhostDuckR.png",
            "ghost_thrust_high_l": "Resources/Images/MontoyaGhostHighThrustL.png",
            "ghost_thrust_high_r": "Resources/Images/MontoyaGhostHighThrustR.png",
            "ghost_thrust_med_l": "Resources/Images/MontoyaGhostMedThrustL.png",
            "ghost_thrust_med_r": "Resources/Images/MontoyaGhostMedThrustR.png",
            "ghost_thrust_low_l": "Resources/Images/MontoyaGhostLowThrustL.png",
            "ghost_thrust_low_r": "Resources/Images/MontoyaGhostLowThrustR.png",
            "ghost_dead_l_1": "Resources/Images/MontoyaGhostDeath1L.png",
            "ghost_dead_r_1": "Resources/Images/MontoyaGhostDeath1R.png",
            "ghost_dead_l_2": "Resources/Images/MontoyaGhostDeath2L.png",
            "ghost_dead_r_2": "Resources/Images/MontoyaGhostDeath2R.png",
            "ghost_dead_l_3": "Resources/Images/MontoyaGhostDeath3L.png",
            "ghost_dead_r_3": "Resources/Images/MontoyaGhostDeath3R.png",
            
            "run_l_1_nosword": "Resources/Images/MontoyaRun1L_nosword.png",
            "run_r_1_nosword": "Resources/Images/MontoyaRun1R_nosword.png",
            "run_l_2_nosword": "Resources/Images/MontoyaRun2L_nosword.png",
            "run_r_2_nosword": "Resources/Images/MontoyaRun2R_nosword.png",
            "run_l_3_nosword": "Resources/Images/MontoyaRun3L_nosword.png",
            "run_r_3_nosword": "Resources/Images/MontoyaRun3R_nosword.png",
            "sword_high_l_nosword": "Resources/Images/MontoyaHighL_nosword.png",
            "sword_high_r_nosword": "Resources/Images/MontoyaHighR_nosword.png",
            "sword_med_l_nosword": "Resources/Images/MontoyaMedL_nosword.png",
            "sword_med_r_nosword": "Resources/Images/MontoyaMedR_nosword.png",
            "sword_low_l_nosword": "Resources/Images/MontoyaLowL_nosword.png",
            "sword_low_r_nosword": "Resources/Images/MontoyaLowR_nosword.png",
            "duck_l_nosword": "Resources/Images/MontoyaDuckL_nosword.png",
            "duck_r_nosword": "Resources/Images/MontoyaDuckR_nosword.png",
            "thrust_high_l_nosword": "Resources/Images/MontoyaHighThrustL_nosword.png",
            "thrust_high_r_nosword": "Resources/Images/MontoyaHighThrustR_nosword.png",
            "thrust_med_l_nosword": "Resources/Images/MontoyaMedThrustL_nosword.png",
            "thrust_med_r_nosword": "Resources/Images/MontoyaMedThrustR_nosword.png",
            "thrust_low_l_nosword": "Resources/Images/MontoyaLowThrustL_nosword.png",
            "thrust_low_r_nosword": "Resources/Images/MontoyaLowThrustR_nosword.png",
            "ghost_run_l_1_nosword": "Resources/Images/MontoyaGhostRun1L_nosword.png",
            "ghost_run_r_1_nosword": "Resources/Images/MontoyaGhostRun1R_nosword.png",
            "ghost_run_l_2_nosword": "Resources/Images/MontoyaGhostRun2L_nosword.png",
            "ghost_run_r_2_nosword": "Resources/Images/MontoyaGhostRun2R_nosword.png",
            "ghost_run_l_3_nosword": "Resources/Images/MontoyaGhostRun3L_nosword.png",
            "ghost_run_r_3_nosword": "Resources/Images/MontoyaGhostRun3R_nosword.png",
            "ghost_sword_high_l_nosword": "Resources/Images/MontoyaGhostHighL_nosword.png",
            "ghost_sword_high_r_nosword": "Resources/Images/MontoyaGhostHighR_nosword.png",
            "ghost_sword_med_l_nosword": "Resources/Images/MontoyaGhostMedL_nosword.png",
            "ghost_sword_med_r_nosword": "Resources/Images/MontoyaGhostMedR_nosword.png",
            "ghost_sword_low_l_nosword": "Resources/Images/MontoyaGhostLowL_nosword.png",
            "ghost_sword_low_r_nosword": "Resources/Images/MontoyaGhostLowR_nosword.png",
            "ghost_duck_l_nosword": "Resources/Images/MontoyaGhostDuckL_nosword.png",
            "ghost_duck_r_nosword": "Resources/Images/MontoyaGhostDuckR_nosword.png",
            "ghost_thrust_high_l_nosword": "Resources/Images/MontoyaGhostHighThrustL_nosword.png",
            "ghost_thrust_high_r_nosword": "Resources/Images/MontoyaGhostHighThrustR_nosword.png",
            "ghost_thrust_med_l_nosword": "Resources/Images/MontoyaGhostMedThrustL_nosword.png",
            "ghost_thrust_med_r_nosword": "Resources/Images/MontoyaGhostMedThrustR_nosword.png",
            "ghost_thrust_low_l_nosword": "Resources/Images/MontoyaGhostLowThrustL_nosword.png",
            "ghost_thrust_low_r_nosword": "Resources/Images/MontoyaGhostLowThrustR_nosword.png"
        }
    return images_dictionary
