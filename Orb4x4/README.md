# Cube Orb 4x4
<img src="https://github.com/geekmomprojects/CubeSphere/blob/main/Orb4x4/Pictures/Illuminated4x4.jpg" width="300">

Please note that this is NOT a detailed tutorial. I have included as much information as I can to help others build
this project, but the design may still evolve, and there is likely room for improvement. It is a challenging build
because the space inside the matrix cube does not leave much room for soldering or electronics. Careful wire
management and good soldering skills will be required.

To make a an LED orb based on 4x4 matrices print each of the STL files in this directory in the quantities listed in the name. You can buy standard 4x4 WS2812 LED matrices on Amazon or AliExpress. This design is intended for matrices taht are approximately 30mm square with 4 mounting holes spaced about 15mm apart. See the [!Pictures](/Pictures) folder for images showing how the interior supports should hold the matrices together.

Everything should be secured together with 5mm M2 flathead (*important*) screws and nuts.

The magnet holders will latch the body of the cube to the lid, using cylindrical magnets with 1/4" diameter and 1/8" height. I designed the magnet holders to work with these countersunk magnet pairs from K&J magnetics (https://www.kjmagnetics.com/proddetail.asp?prod=R422CS-P-N52&cat=15f), with two pair of magnets per cube. The K&J magnets can be held in place with 5mm or 6mm (better) M2 screws and nuts. However, you can also probably buy standard 1/4" diameter, 1/8" height disk magnets and simply glue them into the holders with superglue. I haven't tried it, but I see no reason it shouldn't work.

Everything except the tiles STL should print well at 0.2mm layer height. The tiles have a bit of overhang near the top where it mushrooms out. I printed those at variable layer height with the shortest layers possible at the overhang, which helped a lot. Since there are 16 individual, small tiles in the tiles STL file, printing it can be tricky. Make SURE your first layer goes down ok. If any one of the tiles lifts off, it will ruin the whole print.

I used PETG for all the printing, because the parts are thin and small. Haven't tried it with PLA. PLA should be ok for the tiles, as they don't support anything but the rest of the pieces are small and/or thin, and will probably benefit from using PETG. Use opaque filament for the shell and transparent filament for the tiles. The brackets/holders can be printed in any color/opacity, as they will not be visible.

Once printed, glue each of the tiles into the appropriate locations in the Shell. Gorilla Glue Super Glue Gel strongly is recommended for this purpose. Put small beads or lines of glue in each of the holes in the top of the shell then insert each tile in the appropriate hole. Don't put the glue directly on the tile, because that's much messier (I speak from experience here!). As the tiles look nearly identical, I strongly recommend leaving them on the print plate until just before gluing each one (I loosened them row by row). Make sure to keep the orientation of each tile straight when you glue them, because it matters and it's easy to get them turned around when you lift them off the plate.

Before attaching the shell pieces to the matrix, connect the matrices into the body of the cube and the lid with the connetors as shown in the images in this directory. There are gaps between the matrices by design, as this leaves more room to put a battery inside the cube. You will probably want to solder wires between the matrices as you connect each one to assembly because there is not a lot of room to work inside the body of the fully assembled cube.

Once you have fully assembled the body and lid of the cube, you can attach the shell pieces to each matrix (after the glue for the tiles has fully dried). I placed rows and columns of 2mm wide double-sided tape (https://www.amazon.com/gp/product/B019OQ4Z10/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1) along the bottom of each shell piece, then pressed each one onto a matrix. This works very well, and allows the shells to be removed if necessary. If you are certain that you won't want to remove the shells, then glue should work for this purpose as well. 

A 250 mAh LiPo battery and QTPy-sized controller should fit into the interior of the cube to power everything. Be very careful to cover the exposed pads (tape works for this) so no shorts will occur if a nut or screw becomes loose inside the cube.

I have also included the design for a 14250 cylindrical LiIon battery holder which will fit inside the cube as shown in the picture. This holder is designed to use an AAA battery spring contact no more than 10mm wide (e.g.: https://www.amazon.com/uxcell-Positive-Negative-Conversion-Nickeling/dp/B07HRS5DMC/ref=sr_1_3) for the negative battery terminal and wire wrapped around the hole in the positive terminal to run power to the electronics. More assembly instructions for the battery will follow eventually.

Good luck! Have fun!
