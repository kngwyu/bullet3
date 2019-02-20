import sys
sys.path.append(".")
import dump

header = """/* Copyright (C) 2011 Erwin Coumans & Charlie C
*
* This software is provided 'as-is', without any express or implied
* warranty.  In no event will the authors be held liable for any damages
* arising from the use of this software.
*
* Permission is granted to anyone to use this software for any purpose,
* including commercial applications, and to alter it and redistribute it
* freely, subject to the following restrictions:
*
* 1. The origin of this software must not be misrepresented; you must not
*    claim that you wrote the original software. If you use this software
*    in a product, an acknowledgment in the product documentation would be
*    appreciated but is not required.
* 2. Altered source versions must be plainly marked as such, and must not be
*    misrepresented as being the original software.
* 3. This notice may not be removed or altered from any source distribution.
*/
// Auto generated from Bullet/Extras/HeaderGenerator/bulletGenerate.py
"""

dtList = dump.DataTypeList

out = "autogenerated/"
spaces = 4


def addSpaces(file, space):
    for i in range(0, space):
        file.write(" ")


def write(file, spaces, string):
    addSpaces(file, spaces)
    file.write(string)


###################################################################################
blender = open(out + "bullet.h", 'w')
blender.write(header)
blender.write("#ifndef __BULLET_H__\n")
blender.write("#define __BULLET_H__\n")
#for dt in dtList:
#	blender.write("struct %s;\n"%dt.filename)

###################################################################################

blender.write("namespace Bullet {\n")

strUnRes = """
// put an empty struct in the case
typedef struct bInvalidHandle {
	int unused;
}bInvalidHandle;

"""
blender.write(strUnRes)

for dt in dtList:
    write(blender, 4, "class %s;\n" % dt.name)

for dt in dtList:

    strUpper = dt.filename.upper()

    blender.write("// -------------------------------------------------- //\n")

    write(blender, 4, "class %s\n" % dt.name)

    write(blender, 4, "{\n")
    write(blender, 4, "public:\n")
    for i in dt.dataTypes:
        write(blender, 8, i + ";\n")

    write(blender, 4, "};\n")

    blender.write("\n\n")

blender.write("}\n")
blender.write("#endif//__BULLET_H__")
blender.close()
