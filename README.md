# The Cube Orb Project

Design files and code for a 3D printed shell to transform an LED cube of off-the shelf matrices into an illuminated sphere.

<img src="https://github.com/geekmomprojects/CubeSphere/blob/main/Orb8x8/WS2812/Pictures/CubeWithOrb8x8.jpg" height=300> | <img src="https://github.com/geekmomprojects/CubeSphere/blob/main/Pictures/ThreeOrbs.jpg" height=300>

There are multiple versions of ths project which use off-the shelf matrices of different sizes. Most use WS2812 addressable LEDs, but one version of the 8x8 orb uses SK9822 matrices. The 5x5 Orb is written up in great detail in Make: Magazine, vol. 84.



The designs, which exist in varying degrees of completion are:
- [4x4 WS2812 matrices V1](https://github.com/geekmomprojects/CubeSphere/tree/main/Orb4x4) (challenging)
- [4x4 WS2812 matrices V2 with 3D printed battery holder](https://github.com/geekmomprojects/CubeSphere/tree/main/Orb4x4_V2) (challenging)
- [5x5 WS2812 matrices](https://github.com/geekmomprojects/CubeSphere/tree/main/Orb5x5) (intermediate)
- [8x8 WS2812 matrices](https://github.com/geekmomprojects/CubeSphere/tree/main/Orb8x8/WS2812) (challenging)
- [8x8 SK9822 (APA102 equivalent) matrices](https://github.com/geekmomprojects/CubeSphere/tree/main/Orb8x8/SK9822) (intermediate)

The 8x8 orbs both use the [Pixelblaze Controller](https://electromage.com/pixelblaze) and its associated sensor board to generate pixel-mapped LEDs patterns that are sound/motion responsive. The other orb designs use the [XIAO Sense nRF52840 board](https://www.seeedstudio.com/Seeed-XIAO-BLE-Sense-nRF52840-p-5253.html) with custom CircuitPython code to control the LEDs.

For all designs, it is strongly recommended that you 3D print the cube interior connectors in PETG or other similarly strong filament. The exterior shell may be printed in PETG or PLA. You will need a well-tuned printer with good bed adhesion for this project, especially for the translucent diffusing tiles, as they require printing a large quantity of tiny parts.

