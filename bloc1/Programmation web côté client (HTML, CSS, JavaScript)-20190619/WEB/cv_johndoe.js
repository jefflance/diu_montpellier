var largeurImage;
var hauteurImage;

function zoom(image) {
    largeurImage = image.style.width;
    hauteurImage = image.style.height;

    image.style.width = '50%';
    image.style.height = '50%';
}

function dezoom(image) {
    image.style.width = largeurImage;
    image.style.height = hauteurImage;
}
