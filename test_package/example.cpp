#include <iostream>

#include <fontconfig/fontconfig.h>

int main() {
	FcConfig* config = FcInitLoadConfigAndFonts();
	std::cout << "The death star is complete!" << std::endl;
    return EXIT_SUCCESS;
}
