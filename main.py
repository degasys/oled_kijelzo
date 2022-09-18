feny = 0
basic.show_string("Hello!")
temp = input.temperature()

def on_forever():
    global feny, temp
    basic.show_icon(IconNames.HEART)
    basic.pause(500)
    basic.clear_screen()
    basic.pause(200)
    feny = input.light_level()
    temp = input.temperature()
    OLED.init(128, 64)
    OLED.write_string("Hello ! ")
    OLED.new_line()
    OLED.write_string("A Homerseklet: ")
    OLED.write_num_new_line(temp)
    OLED.write_string(" Celsius fok")
    OLED.new_line()
    OLED.write_string("A fenyerosseg: ")
    OLED.write_num_new_line(feny)
basic.forever(on_forever)
