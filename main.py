numar = 5
if numar % 2 == 0:
    basic.show_icon(IconNames.NO)
    basic.show_string("Par")
else:
    basic.show_icon(IconNames.YES)
    basic.show_string("Impar")
numar = 2
if numar % 2 == 0:
    basic.show_icon(IconNames.YES)
    basic.show_string("Par")
else:
    basic.show_icon(IconNames.NO)
    basic.show_string("Impar")