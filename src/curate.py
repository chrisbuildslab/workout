"""Builds src/exercises.json and sp/*.jpg from free-exercise-db.
Usage: python3 src/curate.py path/to/free-exercise-db

FR maps a free-exercise-db id to (French name, short French cue). Add an entry to add an exercise."""
FR = {
# Chest
"Barbell_Bench_Press_-_Medium_Grip": ("Développé couché barre", "Omoplates serrées, descends la barre au bas des pecs, pousse en expirant."),
"Barbell_Incline_Bench_Press_-_Medium_Grip": ("Développé incliné barre", "Banc à 30-45°, barre vers le haut des pecs, coudes à ~45°."),
"Decline_Barbell_Bench_Press": ("Développé décliné barre", "Banc décliné, barre vers le bas des pecs, contrôle la descente."),
"Dumbbell_Bench_Press": ("Développé couché haltères", "Haltères au niveau de la poitrine, pousse en rapprochant légèrement en haut."),
"Incline_Dumbbell_Press": ("Développé incliné haltères", "Banc à 30-45°, descends les haltères sur les côtés du haut des pecs."),
"Decline_Dumbbell_Bench_Press": ("Développé décliné haltères", "Banc décliné, poussée verticale contrôlée."),
"Dumbbell_Flyes": ("Écarté couché haltères", "Bras légèrement fléchis, ouvre en arc jusqu'à l'étirement, referme."),
"Incline_Dumbbell_Flyes": ("Écarté incliné haltères", "Comme l'écarté couché, sur banc incliné pour le haut des pecs."),
"Cable_Crossover": ("Écarté à la poulie vis-à-vis", "Poulies hautes, ramène les mains devant le bas de la poitrine."),
"Low_Cable_Crossover": ("Écarté poulie basse", "Poulies basses, ramène les mains vers le haut devant le visage."),
"Butterfly": ("Pec deck (butterfly)", "Dos plaqué, rapproche les bras devant toi, retour lent."),
"Machine_Bench_Press": ("Développé couché machine", "Poignées à hauteur de poitrine, pousse sans verrouiller les coudes."),
"Leverage_Incline_Chest_Press": ("Développé incliné machine", "Pousse vers le haut et l'avant, omoplates en arrière."),
"Smith_Machine_Bench_Press": ("Développé couché Smith", "Barre guidée vers le milieu des pecs."),
"Pushups": ("Pompes", "Corps gainé et aligné, poitrine près du sol, pousse."),
"Push-Up_Wide": ("Pompes mains larges", "Mains plus larges que les épaules, accent sur les pecs."),
"Push-Ups_With_Feet_Elevated": ("Pompes pieds surélevés", "Pieds sur un banc, accent sur le haut des pecs."),
"Incline_Push-Up": ("Pompes inclinées (mains surélevées)", "Mains sur un banc : version plus facile des pompes."),
"Dips_-_Chest_Version": ("Dips (pectoraux)", "Buste penché en avant, coudes écartés, descends jusqu'à l'étirement."),
"Straight-Arm_Dumbbell_Pullover": ("Pull-over haltère", "Allongé, haltère au-dessus de la poitrine, descends derrière la tête bras tendus."),
"Cable_Chest_Press": ("Développé poulie debout", "Dos aux poulies, pousse les poignées vers l'avant."),
# Back
"Pullups": ("Tractions pronation", "Prise large paumes vers l'avant, monte le menton au-dessus de la barre."),
"Chin-Up": ("Tractions supination", "Paumes vers toi, prise largeur d'épaules, poitrine vers la barre."),
"Band_Assisted_Pull-Up": ("Tractions assistées élastique", "Élastique sous les genoux pour alléger le poids du corps."),
"Weighted_Pull_Ups": ("Tractions lestées", "Tractions avec ceinture de lest."),
"Wide-Grip_Lat_Pulldown": ("Tirage vertical prise large", "Tire la barre vers le haut de la poitrine, coudes vers le bas."),
"Close-Grip_Front_Lat_Pulldown": ("Tirage vertical prise serrée", "Prise serrée, tire vers la poitrine en sortant le torse."),
"V-Bar_Pulldown": ("Tirage vertical poignée triangle", "Poignée en V, tire vers le haut du ventre/poitrine."),
"Underhand_Cable_Pulldowns": ("Tirage vertical supination", "Paumes vers toi, tire vers la poitrine."),
"Straight-Arm_Pulldown": ("Pull-over poulie bras tendus", "Bras tendus, ramène la barre vers les cuisses en contractant les dorsaux."),
"Seated_Cable_Rows": ("Tirage horizontal assis (poulie)", "Dos droit, tire la poignée vers le ventre, omoplates serrées."),
"Bent_Over_Barbell_Row": ("Rowing barre buste penché", "Buste à ~45°, dos plat, tire la barre vers le nombril."),
"Reverse_Grip_Bent-Over_Rows": ("Rowing barre supination", "Comme le rowing barre, paumes vers le haut."),
"One-Arm_Dumbbell_Row": ("Rowing un bras haltère", "Genou et main sur le banc, tire l'haltère vers la hanche."),
"Bent_Over_Two-Dumbbell_Row": ("Rowing deux haltères", "Buste penché, tire les deux haltères vers les hanches."),
"Dumbbell_Incline_Row": ("Rowing haltères sur banc incliné", "Poitrine sur banc incliné, tire les haltères."),
"T-Bar_Row_with_Handle": ("Rowing T-bar", "Buste penché, tire la poignée vers la poitrine."),
"Lying_T-Bar_Row": ("Rowing T-bar allongé (machine)", "Poitrine sur le support, tire vers toi."),
"Leverage_High_Row": ("Tirage haut machine", "Tire les poignées vers toi en serrant les omoplates."),
"Bodyweight_Mid_Row": ("Rowing inversé (poids du corps)", "Sous une barre basse, tire la poitrine vers la barre, corps gainé."),
"Face_Pull": ("Face pull", "Corde à hauteur du visage, tire vers le front en écartant les mains."),
"Barbell_Deadlift": ("Soulevé de terre", "Dos plat, barre près des tibias, pousse dans le sol et tends hanches et genoux."),
"Trap_Bar_Deadlift": ("Soulevé de terre trap bar", "Debout dans la barre hexagonale, pousse avec les jambes, dos neutre."),
"Rack_Pulls": ("Rack pull (soulevé partiel)", "Barre sur supports à hauteur des genoux, verrouille les hanches."),
"Hyperextensions_Back_Extensions": ("Extensions lombaires (banc)", "Hanches sur le banc, descends le buste puis remonte jusqu'à l'alignement."),
"Good_Morning": ("Good morning", "Barre sur le dos, genoux souples, penche le buste dos plat puis remonte."),
"Barbell_Shrug": ("Haussements d'épaules barre", "Bras tendus, monte les épaules vers les oreilles, pause, redescends."),
"Dumbbell_Shrug": ("Haussements d'épaules haltères", "Haltères le long du corps, monte les épaules."),
# Shoulders
"Standing_Military_Press": ("Développé militaire debout", "Barre devant le cou, pousse au-dessus de la tête, fessiers et abdos serrés."),
"Seated_Barbell_Military_Press": ("Développé militaire assis", "Assis dos calé, pousse la barre au-dessus de la tête."),
"Dumbbell_Shoulder_Press": ("Développé épaules haltères", "Haltères à hauteur d'oreilles, pousse au-dessus de la tête."),
"Seated_Dumbbell_Press": ("Développé haltères assis", "Assis dos droit, pousse les haltères vers le haut."),
"Arnold_Dumbbell_Press": ("Développé Arnold", "Paumes vers toi en bas, tourne les poignets en poussant vers le haut."),
"Machine_Shoulder_Military_Press": ("Développé épaules machine", "Poignées à hauteur d'épaules, pousse vers le haut."),
"Side_Lateral_Raise": ("Élévations latérales", "Bras légèrement fléchis, monte les haltères sur les côtés jusqu'aux épaules."),
"Cable_Seated_Lateral_Raise": ("Élévation latérale poulie", "Poulie basse, monte le bras sur le côté."),
"Front_Dumbbell_Raise": ("Élévations frontales haltères", "Monte les haltères devant toi jusqu'à hauteur d'yeux."),
"Front_Plate_Raise": ("Élévation frontale disque", "Disque tenu à deux mains, monte devant toi."),
"Reverse_Flyes": ("Oiseau haltères", "Buste penché, ouvre les bras sur les côtés (arrière d'épaule)."),
"Reverse_Machine_Flyes": ("Oiseau machine (reverse pec deck)", "Face à la machine, écarte les bras vers l'arrière."),
"Cable_Rear_Delt_Fly": ("Oiseau poulie", "Poulies croisées, écarte les bras vers l'arrière."),
"Upright_Barbell_Row": ("Rowing menton barre", "Tire la barre le long du corps jusqu'à la poitrine, coudes hauts."),
"External_Rotation_with_Cable": ("Rotation externe poulie", "Coude collé au corps, tourne l'avant-bras vers l'extérieur."),
# Biceps
"Barbell_Curl": ("Curl barre", "Coudes fixes le long du corps, monte la barre sans balancer."),
"EZ-Bar_Curl": ("Curl barre EZ", "Barre coudée pour soulager les poignets, coudes fixes."),
"Dumbbell_Bicep_Curl": ("Curl haltères", "Monte les haltères en tournant les paumes vers le haut."),
"Dumbbell_Alternate_Bicep_Curl": ("Curl haltères alterné", "Un bras après l'autre, coudes fixes."),
"Hammer_Curls": ("Curl marteau", "Paumes face à face, monte les haltères."),
"Incline_Dumbbell_Curl": ("Curl incliné haltères", "Assis sur banc incliné, bras pendants, monte les haltères."),
"Concentration_Curls": ("Curl concentré", "Assis, coude contre l'intérieur de la cuisse, monte l'haltère."),
"Preacher_Curl": ("Curl pupitre (Larry Scott)", "Bras sur le pupitre, monte la barre sans décoller les bras."),
"Machine_Preacher_Curls": ("Curl pupitre machine", "Bras sur l'appui, fléchis les coudes."),
"Standing_Biceps_Cable_Curl": ("Curl poulie basse", "Face à la poulie basse, monte la barre coudes fixes."),
"Cable_Hammer_Curls_-_Rope_Attachment": ("Curl marteau à la corde", "Corde à la poulie basse, prise neutre."),
"Spider_Curl": ("Spider curl", "Poitrine contre banc incliné, bras pendants, curl."),
"Reverse_Barbell_Curl": ("Curl inversé barre", "Paumes vers le bas, travaille avant-bras et biceps."),
"Zottman_Curl": ("Curl Zottman", "Monte paumes vers le haut, tourne et redescends paumes vers le bas."),
# Triceps
"Triceps_Pushdown": ("Extension triceps poulie haute (barre)", "Coudes collés, pousse la barre vers le bas jusqu'à extension."),
"Triceps_Pushdown_-_Rope_Attachment": ("Extension triceps à la corde", "Corde à la poulie haute, écarte les mains en bas."),
"Reverse_Grip_Triceps_Pushdown": ("Extension triceps prise inversée", "Paumes vers le haut, pousse vers le bas."),
"Cable_Rope_Overhead_Triceps_Extension": ("Extension triceps au-dessus de la tête (corde)", "Dos à la poulie, tends les bras au-dessus de la tête."),
"EZ-Bar_Skullcrusher": ("Barre au front", "Allongé, descends la barre vers le front en pliant les coudes, remonte."),
"Lying_Dumbbell_Tricep_Extension": ("Extension triceps allongé haltères", "Allongé, haltères descendus à côté de la tête."),
"Standing_Dumbbell_Triceps_Extension": ("Extension triceps haltère debout", "Haltère à deux mains derrière la tête, tends les bras."),
"Seated_Triceps_Press": ("Extension triceps assis", "Assis, haltère derrière la tête, tends les bras."),
"Tricep_Dumbbell_Kickback": ("Kickback triceps", "Buste penché, coude haut, tends l'avant-bras vers l'arrière."),
"Close-Grip_Barbell_Bench_Press": ("Développé couché prise serrée", "Mains largeur d'épaules, coudes près du corps."),
"Dips_-_Triceps_Version": ("Dips (triceps)", "Buste droit, coudes vers l'arrière, descends à 90°."),
"Bench_Dips": ("Dips entre deux bancs", "Mains sur un banc derrière toi, descends en pliant les coudes."),
"Push-Ups_-_Close_Triceps_Position": ("Pompes serrées (diamant)", "Mains rapprochées sous la poitrine, coudes le long du corps."),
"Machine_Triceps_Extension": ("Extension triceps machine", "Coudes sur l'appui, tends les bras."),
# Legs
"Barbell_Squat": ("Squat barre", "Barre sur le haut du dos, descends hanches en arrière, genoux dans l'axe des pieds."),
"Barbell_Full_Squat": ("Squat complet barre", "Squat en amplitude complète, dos neutre."),
"Front_Barbell_Squat": ("Squat avant (front squat)", "Barre sur l'avant des épaules, buste droit, coudes hauts."),
"Goblet_Squat": ("Goblet squat", "Haltère ou kettlebell contre la poitrine, squat profond buste droit."),
"Dumbbell_Squat": ("Squat haltères", "Haltères le long du corps, squat."),
"Bodyweight_Squat": ("Squat poids du corps", "Bras devant, descends en poussant les hanches en arrière."),
"Box_Squat": ("Box squat", "Descends jusqu'à t'asseoir brièvement sur une box, remonte."),
"Smith_Machine_Squat": ("Squat Smith machine", "Barre guidée, pieds légèrement devant."),
"Hack_Squat": ("Hack squat machine", "Dos contre le dossier, descends jambes fléchies, pousse."),
"Leg_Press": ("Presse à cuisses", "Pieds largeur d'épaules, descends jusqu'à 90°, pousse sans verrouiller."),
"Leg_Extensions": ("Leg extension", "Assis, tends les jambes, pause en haut, redescends lentement."),
"Lying_Leg_Curls": ("Leg curl allongé", "Allongé sur le ventre, ramène les talons vers les fessiers."),
"Seated_Leg_Curl": ("Leg curl assis", "Assis, ramène les talons sous le siège."),
"Standing_Leg_Curl": ("Leg curl debout", "Une jambe à la fois, ramène le talon vers le fessier."),
"Romanian_Deadlift": ("Soulevé de terre roumain", "Genoux légèrement fléchis, pousse les hanches en arrière, barre le long des cuisses."),
"Stiff-Legged_Dumbbell_Deadlift": ("Soulevé de terre jambes tendues haltères", "Jambes presque tendues, dos plat, étire les ischios."),
"Sumo_Deadlift": ("Soulevé de terre sumo", "Pieds écartés, mains à l'intérieur des jambes, buste droit."),
"Dumbbell_Lunges": ("Fentes avant haltères", "Grand pas en avant, genou arrière vers le sol, repousse."),
"Barbell_Lunge": ("Fentes barre", "Barre sur le dos, fente avant."),
"Barbell_Walking_Lunge": ("Fentes marchées", "Enchaîne les fentes en avançant."),
"Dumbbell_Rear_Lunge": ("Fentes arrière haltères", "Recule d'un grand pas, descends, reviens."),
"Split_Squat_with_Dumbbells": ("Squat bulgare / fente statique", "Pied arrière (sur un banc pour le bulgare), descends verticalement."),
"Dumbbell_Step_Ups": ("Step-up haltères", "Monte sur un banc en poussant sur le talon avant."),
"Barbell_Hip_Thrust": ("Hip thrust barre", "Haut du dos sur un banc, barre sur les hanches, monte le bassin, serre les fessiers."),
"Barbell_Glute_Bridge": ("Pont fessier barre", "Au sol, barre sur les hanches, monte le bassin."),
"Single_Leg_Glute_Bridge": ("Pont fessier une jambe", "Une jambe tendue en l'air, monte le bassin sur l'autre."),
"Glute_Kickback": ("Kickback fessier", "À quatre pattes, pousse une jambe vers l'arrière et le haut."),
"One-Legged_Cable_Kickback": ("Kickback poulie", "Cheville attachée à la poulie basse, pousse la jambe vers l'arrière."),
"Pull_Through": ("Pull-through poulie", "Dos à la poulie, corde entre les jambes, extension de hanches."),
"Thigh_Abductor": ("Abducteurs machine", "Assis, écarte les jambes contre la résistance."),
"Thigh_Adductor": ("Adducteurs machine", "Assis, rapproche les jambes contre la résistance."),
"Standing_Calf_Raises": ("Mollets debout (machine)", "Monte sur la pointe des pieds, pause, descends en étirant."),
"Seated_Calf_Raise": ("Mollets assis", "Assis, genoux sous l'appui, monte les talons."),
"Calf_Press_On_The_Leg_Press_Machine": ("Mollets à la presse", "Pointes de pieds en bas du plateau, pousse avec les chevilles."),
"Standing_Dumbbell_Calf_Raise": ("Mollets debout haltères", "Haltères en main, monte sur la pointe des pieds."),
"Glute_Ham_Raise": ("Glute ham raise", "Chevilles bloquées, descends le buste puis remonte avec les ischios."),
# Abs
"Crunches": ("Crunch", "Allongé genoux fléchis, enroule le haut du dos vers le bassin."),
"Plank": ("Gainage (planche)", "Sur les avant-bras, corps aligné, abdos et fessiers serrés."),
"Side_Bridge": ("Gainage latéral", "Sur un avant-bras, corps aligné de côté."),
"Hanging_Leg_Raise": ("Relevés de jambes suspendu", "Suspendu à une barre, monte les jambes sans balancer."),
"Flat_Bench_Lying_Leg_Raise": ("Relevés de jambes allongé", "Sur un banc, monte les jambes tendues à la verticale."),
"Reverse_Crunch": ("Crunch inversé", "Allongé, ramène les genoux vers la poitrine en décollant le bassin."),
"Cable_Crunch": ("Crunch à la poulie", "À genoux, corde derrière la tête, enroule le buste vers le sol."),
"Ab_Roller": ("Roue abdominale", "À genoux, roule vers l'avant en gardant le dos neutre, reviens."),
"Russian_Twist": ("Rotations russes", "Assis buste incliné, tourne le buste d'un côté à l'autre."),
"Sit-Up": ("Sit-up", "Remonte le buste jusqu'aux genoux, redescends contrôlé."),
"Dead_Bug": ("Dead bug", "Sur le dos, tends bras et jambe opposés en gardant le bas du dos au sol."),
"Pallof_Press": ("Pallof press", "De profil à la poulie, pousse la poignée devant toi sans tourner."),
"Standing_Cable_Wood_Chop": ("Bûcheron à la poulie", "Tire la poignée en diagonale de haut en bas en tournant le buste."),
"Ab_Crunch_Machine": ("Crunch machine", "Enroule le buste contre la résistance."),
"Oblique_Crunches_-_On_The_Floor": ("Crunch obliques", "Allongé sur le côté, enroule vers la hanche."),
"Dumbbell_Side_Bend": ("Flexions latérales haltère", "Haltère d'un côté, penche-toi sur le côté puis remonte."),
# Forearms
"Palms-Up_Barbell_Wrist_Curl_Over_A_Bench": ("Curl poignets barre", "Avant-bras sur un banc, monte la barre avec les poignets."),
"Palms-Down_Wrist_Curl_Over_A_Bench": ("Extension des poignets barre", "Paumes vers le bas, monte la barre avec les poignets."),
"Wrist_Roller": ("Rouleau à poignets", "Enroule la corde du poids en tournant la barre."),
}
MUSCLE_FR = {
 "chest":"Pectoraux","lats":"Dos","middle back":"Dos","lower back":"Lombaires","traps":"Trapèzes",
 "shoulders":"Épaules","biceps":"Biceps","triceps":"Triceps","forearms":"Avant-bras",
 "quadriceps":"Quadriceps","hamstrings":"Ischios","glutes":"Fessiers","calves":"Mollets",
 "abductors":"Fessiers","adductors":"Adducteurs","abdominals":"Abdos","neck":"Cou",
}
EQUIP_FR = {"barbell":"Barre","dumbbell":"Haltères","cable":"Poulie","machine":"Machine","body only":"Poids du corps",
 "e-z curl bar":"Barre EZ","kettlebells":"Kettlebell","other":"Autre","bands":"Élastique",None:"Autre","medicine ball":"Médecine-ball","exercise ball":"Swiss ball","foam roll":"Rouleau"}

import json, os, pathlib, sys
from PIL import Image
ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = sys.argv[1] if len(sys.argv) > 1 else "free-exercise-db"  # clone of github.com/yuhonas/free-exercise-db
os.makedirs(ROOT/"sp", exist_ok=True)
d = {x['id']: x for x in json.load(open(f"{SRC}/dist/exercises.json"))}
missing = [k for k in FR if k not in d]
assert not missing, missing
res = []
for k, (name, cue) in FR.items():
    x = d[k]
    # One sprite per exercise: start position left, end position right (420x280 each)
    W, H = 420, 280; sp = Image.new('RGB', (W*2, H), 'white')
    for i, p in enumerate(x['images'][:2]):
        im = Image.open(f"{SRC}/exercises/{p}").convert("RGB"); im.thumbnail((W, H))
        sp.paste(im, (i*W + (W-im.width)//2, (H-im.height)//2))
    fn = f"sp/{k.replace('-', '_')}.jpg"
    sp.save(ROOT/fn, quality=64, optimize=True, progressive=True)
    res.append({"id": k, "n": name, "c": cue, "m": MUSCLE_FR[x['primaryMuscles'][0]],
      "m2": sorted({MUSCLE_FR[m] for m in x['secondaryMuscles']} - {MUSCLE_FR[x['primaryMuscles'][0]]}),
      "e": EQUIP_FR[x['equipment']], "en": x['name'], "steps": x['instructions'], "s": fn})
json.dump(res, open(ROOT/"src/exercises.json", "w"), ensure_ascii=False, separators=(",", ":"))
print(len(res), "exercices")
