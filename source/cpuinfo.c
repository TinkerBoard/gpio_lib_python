/*
Copyright (c) 2012-2015 Ben Croston

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "cpuinfo.h"

int get_asuspi_info(asuspi_info *info)
{
	FILE *fp;
	char buffer[1024];
	char hardware[1024];
	int found = 0;
	char revision[1024];
	if ((fp = fopen("/proc/cpuinfo", "r")) == NULL)
		return -1;
	while(!feof(fp)) 
	{
		if(fgets(buffer, sizeof(buffer) , fp) != NULL);
		sscanf(buffer, "Hardware	: %s", hardware);
		if (strcmp(hardware, "Rockchip") == 0) 
		{
			found = 1;
		}
		sscanf(buffer, "Revision	: %s", revision);

	}
	fclose(fp);

	if (!found)
		return -1;
	info->p1_revision = 3;
	strcpy(info->revision, revision);
	info->type = "Tinker Board";
	info->processor = "ROCKCHIP3288";
	info->manufacturer = "ASUS";
	info->ram = "1024M";

	return 0;
}

