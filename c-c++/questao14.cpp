//Laborat�rio de Prot�tipos - LPROT

#include "opencv\cv.h"
#include "opencv\highgui.h"

using namespace std;
using namespace cv;

Mat gray; 
Mat frame;

int main()
{
    VideoCapture cap(0); //Abrir a camera

	if(!cap.isOpened()) //Prote��o para abertura da camera
		return 0;

    while (1) 
	{

		cap >> frame; //Capturar a imagem 

		cvtColor (frame, gray, CV_RGB2GRAY); //Converter a imagem para tons de cinza

		imshow ("Video", gray); //Mostrar a imagem

		if(waitKey(30) >= 0) //D�vida
			break;
	}

	return 0;
}
 

