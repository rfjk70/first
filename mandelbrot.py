# Mandelbrot fractal displayed in ASCII

def mandelbrot(width=80, height=24, x_center=-0.5, y_center=0.0, zoom=1.0, max_iter=40):
    """Render the Mandelbrot set in ASCII characters."""
    aspect_ratio = width / float(height)
    x_width = 3.5 / zoom
    y_height = x_width / aspect_ratio
    chars = " .:-=+*#%@"

    for y in range(height):
        imag = y_center + (y_height / 2) - y * (y_height / height)
        line = []
        for x in range(width):
            real = x_center - (x_width / 2) + x * (x_width / width)
            c = complex(real, imag)
            z = 0j
            for i in range(max_iter):
                z = z * z + c
                if abs(z) > 2:
                    break
            else:
                i = max_iter - 1
            char_index = int(i / max_iter * (len(chars) - 1))
            line.append(chars[char_index])
        print(''.join(line))

if __name__ == "__main__":
    mandelbrot()
