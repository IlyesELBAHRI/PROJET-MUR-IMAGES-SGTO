extends Node2D


var ecran = 0
#var ecran = 1
var timer=0
var first=1
var videoOn=0
var imageOn=0
var fade=0
var connected = 0
var trame_demandee = 0
var trame_ON = 0
var scale_factor_image = 1
var tab_trame = []
var tok_metro
var tok_bus
var tok_meteo
var tok_trame

# Called when the node enters the scene tree for the first time.
func _ready():
	OS.window_fullscreen = true
	OS.window_position = Vector2(0,0)
	OS.window_size = Vector2(2560, 1600)
	OS.window_maximized = true
	$Control/Label.raise()
	$Control/Labels_Metro.raise()
	$Control/Label.set_scale(Vector2(5,5))
	$Control/VideoPlayer.set_size(get_viewport_rect().size)

	#serverAddress="127.0.0.1"
	#serverAddress="192.168.1.10"
	#serverAddress="192.168.1.12"

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	timer+=delta
	if (timer>=3) and (first==1):
		first=0
		connected = 1
	
	elif trame_ON == 0 and imageOn == 0 and connected == 1:
		$Control/VideoPlayer.visible = false
		if ecran == 0:
			display_metro()
			while imageOn:
				yield(get_tree(), "idle_frame")
			$Control/Labels_Metro.visible = false
			display_bus()
			while imageOn:
				yield(get_tree(), "idle_frame")
			$Control/Labels_Bus.visible = false
		if ecran == 1:
			display_meteo()
			while imageOn:
				yield(get_tree(), "idle_frame")
			$Control/Labels_Meteo.visible = false

		display_trame()
		
func get_meteo():
	# Ouvrir le fichier texte
	var file = File.new()
	var error = file.open("src/data_meteo.txt", File.READ)
	if error != OK:
		print("Erreur lors de l'ouverture du fichier :", error)
	else:
		# Lire la première ligne
		var line = file.get_line()
		# Récupérer chaque chiffre de la ligne
		tok_meteo = line.split("-")
		print(tok_meteo)
		# Fermer le fichier
		file.close()

func get_metro_time():
	# Ouvrir le fichier texte
	var file = File.new()
	var error = file.open("src/data_metro.txt", File.READ)
	if error != OK:
		print("Erreur lors de l'ouverture du fichier :", error)
	else:
		# Lire la première ligne
		var line = file.get_line()
		# Récupérer chaque chiffre de la ligne
		tok_metro = line.split(" ")
		print(tok_metro)
		# Fermer le fichier
		file.close()
	
func get_bus_time():
	# Ouvrir le fichier texte
	var file = File.new()
	var error = file.open("src/data_bus.txt", File.READ)
	if error != OK:
		print("Erreur lors de l'ouverture du fichier :", error)
	else:
		# Lire la première ligne
		var line = file.get_line()
		# Récupérer chaque chiffre de la ligne
		tok_bus = line.split(" ")
		print(tok_bus)
		# Fermer le fichier
		file.close()

func get_trame():
	# Ouvrir le fichier texte
	var file = File.new()
	var error = file.open("src/config.txt", File.READ)
	if error != OK:
		print("Erreur lors de l'ouverture du fichier :", error)
	else:
		if ecran == 0:
			# Lire la première ligne
			var line1 = file.get_line()
			# Récupérer chaque donnee de la ligne
			tok_trame = line1.split(" ")
			tab_trame.append(tab_trame)
			print(tok_trame)
			# Fermer le fichier
			file.close()
		if ecran == 1:
			# Lire la deuxième ligne
			var line1 = file.get_line()
			var line2 = file.get_line()
			# Récupérer chaque donnee de la ligne
			tok_trame = line2.split(" ")
			tab_trame.append(tab_trame)
			print(tok_trame)
			# Fermer le fichier
			file.close()
	
func display_metro():				
	$Control/Sprite.set_texture(ResourceLoader.load("src/metro.jpeg"))
	$Control/Sprite.set_scale(Vector2(get_viewport_rect().size.x/$Control/Sprite.texture.get_size().x, get_viewport_rect().size.y/$Control/Sprite.texture.get_size().y))
	get_metro_time()
	$Control/Labels_Metro/Metro7_1.set_text(tok_metro[1])
	$Control/Labels_Metro/Metro7_2.set_text(tok_metro[2])
	$Control/Labels_Metro/Metro7_3.set_text(tok_metro[3])
	$Control/Labels_Metro/Metro7_4.set_text(tok_metro[4])
	$Control/Labels_Metro/Metro7_5.set_text(tok_metro[5])
	$Control/Labels_Metro/Metro7_6.set_text(tok_metro[6])
	$Control/Labels_Metro/Metro10_1.set_text(tok_metro[7])
	$Control/Labels_Metro/Metro10_2.set_text(tok_metro[8])
	$Control/Labels_Metro/Metro10_3.set_text(tok_metro[9])
	$Control/Labels_Metro/Metro10_4.set_text(tok_metro[10])
	$Control/Labels_Metro.visible = true
	start_timer(10, $Control/Sprite)

func display_bus():
	$Control/Sprite.set_texture(ResourceLoader.load("src/bus.jpeg"))
	$Control/Sprite.set_scale(Vector2(get_viewport_rect().size.x/$Control/Sprite.texture.get_size().x, get_viewport_rect().size.y/$Control/Sprite.texture.get_size().y))
	get_bus_time()
	$Control/Labels_Bus/Bus89_1.set_text(tok_bus[1])
	$Control/Labels_Bus/Bus89_2.set_text(tok_bus[2])
	$Control/Labels_Bus/Bus89_3.set_text(tok_bus[3])
	$Control/Labels_Bus/Bus89_4.set_text(tok_bus[4])
	$Control/Labels_Bus/Bus67_1.set_text(tok_bus[5])
	$Control/Labels_Bus/Bus67_2.set_text(tok_bus[6])
	$Control/Labels_Bus/Bus67_3.set_text(tok_bus[7])
	$Control/Labels_Bus/Bus67_4.set_text(tok_bus[8])
	$Control/Labels_Bus/Bus63_1.set_text(tok_bus[9])
	$Control/Labels_Bus/Bus63_2.set_text(tok_bus[10])
	$Control/Labels_Bus/Bus63_3.set_text(tok_bus[11])
	$Control/Labels_Bus/Bus63_4.set_text(tok_bus[12])
	$Control/Labels_Bus.visible = true
	start_timer(10, $Control/Sprite)
		
func display_meteo():
	$Control/Sprite.set_texture(ResourceLoader.load("src/meteo.png"))
	$Control/Sprite.set_scale(Vector2(get_viewport_rect().size.x/$Control/Sprite.texture.get_size().x, get_viewport_rect().size.y/$Control/Sprite.texture.get_size().y))
	get_meteo()
	$Control/Labels_Meteo/Jour1_1.set_text(tok_meteo[1])
	$Control/Labels_Meteo/Jour1_2.set_text(tok_meteo[2])
	$Control/Labels_Meteo/Jour1_3.set_text(tok_meteo[3])
	$Control/Labels_Meteo/Jour2_1.set_text(tok_meteo[4])
	$Control/Labels_Meteo/Jour2_2.set_text(tok_meteo[5])
	$Control/Labels_Meteo/Jour2_3.set_text(tok_meteo[6])
	$Control/Labels_Meteo/Jour3_1.set_text(tok_meteo[7])
	$Control/Labels_Meteo/Jour3_2.set_text(tok_meteo[8])
	$Control/Labels_Meteo/Jour3_3.set_text(tok_meteo[9])
	$Control/Labels_Meteo.visible = true
	start_timer(10, $Control/Sprite)

func display_trame():
	trame_ON = 1
	get_trame()
	for i in range(2, tok_trame.size()):
		if tok_trame[i] == "V" and imageOn == 0:
			$Control/VideoPlayer.visible = true
			print("afficher une video")
			i += 1
			var file_name = tok_trame[i]
			print(file_name)
			$Control/VideoPlayer.stream = load(file_name)
			
			yield(get_tree().create_timer(1), "timeout")
		
			#$Control/VideoPlayer.set_stream(load(file_name)) 
			$Control/VideoPlayer.play()
			while $Control/VideoPlayer.is_playing():
				#$Control/Label.set_text("Video Playing")
				yield(get_tree(), "idle_frame")
			$Control/VideoPlayer.stop()
		elif tok_trame[i] == "I" and $Control/VideoPlayer.is_playing()==false and imageOn == 0:
			$Control/VideoPlayer.visible = false
			print("afficher une image")
			i += 1
			var file_name = tok_trame[i]
			$Control/Sprite.set_texture(ResourceLoader.load(file_name))
			$Control/Sprite.set_scale(Vector2(get_viewport_rect().size.x/$Control/Sprite.texture.get_size().x, get_viewport_rect().size.y/$Control/Sprite.texture.get_size().y))
			i += 1
			var display_time = float(tok_trame[i])
			#$Control/Label.set_text("Image displayed for " + str(display_time) + " sec")
			start_timer(display_time, $Control/Sprite)
			while imageOn:
				yield(get_tree(), "idle_frame")
	trame_ON = 0

	
func _input(event):
	if event is InputEventKey and event.scancode == KEY_ESCAPE:
		get_tree().quit()

func start_timer(time, obj):
	imageOn = 1
	fade_in(obj,$Control/Sprite/Tween,1)
	print("apparition image")
	yield(get_tree().create_timer(time), "timeout")
	fade_out(obj,$Control/Sprite/Tween,1)
	yield(get_tree().create_timer(1), "timeout") # attendre une seconde pour que l'effet de fondu se termine
	print("disparition image")
	imageOn = 0
	

#Fait disparaître l'objet avec un effet fondu
func fade_out(obj,tween,duration):
	tween.interpolate_property(obj, "modulate", obj.modulate, Color(1, 1, 1, 0), duration, Tween.TRANS_LINEAR, Tween.EASE_OUT)
	tween.start()
	obj.set_process_input(false)
	obj.set_process(false)


#Fait réapparaître l'objet avec un effet fondu
func fade_in(obj,tween,duration):
	tween.interpolate_property(obj, "modulate", obj.modulate, Color(1, 1, 1, 1), duration, Tween.TRANS_LINEAR, Tween.EASE_IN)
	tween.start()
	obj.set_process_input(true)
	obj.set_process(true)
