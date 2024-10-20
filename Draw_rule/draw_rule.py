def draw_line(tick_length, tick_lable=''):
    line = '-' * tick_length
    if tick_lable:
        line += ' ' + tick_lable
    print(line)

def draw_interval(center_length):
    if center_length > 0:
        draw_interval(center_length - 1)
        draw_line(center_length)
        draw_interval(center_length - 1)

def draw_rule(nums_inches, maior_length):
    draw_line(maior_length, '0')
    for i in range(1, 1 + nums_inches):
        draw_interval(maior_length - 1)
        draw_line(maior_length, str(i))
        
draw_rule(1, 3)