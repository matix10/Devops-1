Web App Deployment using minikube

El equipo de desarrollo de la empresa esta trabajando en una nueva aplicacion web. 
Una primera version del mismo ha sido subida a DockerHub y vamos a desplegarla en Kubernetes

Vamos a desplegar esta primera versión de la aplicación, para ello:

Crea un archivo yaml (puedes usar el de la actividad anterior) para desplegar la imagen: roxsross12/k8s_test_web:v1 (Utilizamos una imagen de roxsross)

Crea el Deployment, recuerda realizar una anotación para indicar las características del despliegue.

Crea una redirección utilizando el port-forward para acceder a la aplicación, sabiendo que la aplicación ofrece el servicio en el puerto 80, y accede a la aplicación con un navegador web.

![alt text](image.png)