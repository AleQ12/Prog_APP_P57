clc; clear all; close all;
%Insertar Usuarios
N=input('Ingrese N(Celulares):');
x=rand(N,1); y=rand(N,1);
hold on
plot(x,y,'bx');
for j=1:N      %Nombra a cada usuario
       te=text(x(j)+0.01,y(j)+0.01,sprintf('u%d',j));  
end
disp('UBICACION DE ANTENAS') 
xrsu=[]; yrsu=[];
boton=1;
axis([0 2 0 2])
img=imread('ups.png');
theta=linspace(0,5*pi,200);
image('CData',img,'XData',[0 2],'YData',[2 0]);
axis on

%Insetar Antenas
while boton==1
    [xo,yo,boton]=ginput(2);
    xrsu=[xrsu xo]; yrsu=[yrsu yo];
    plot(xrsu,yrsu,'r.','markersize',25); 
    title(sprintf('ANTENAS %d', length(xrsu))); 
end
M=length(xrsu);   
 for i=1:M      %Nombra a cada RSU
        te=text(xrsu(i)+0.01, yrsu(i)+0.01,sprintf('A%d',i)); 
 end    
 
%Conexiones con Distancias
for i=1:length(xrsu)
    for j=1:length(x)
        dist(i,j)=sqrt((xrsu(i)-x(j))^2+(yrsu(i)-y(j))^2);
        if(dist(i,j)<=0.2)
        plot([xrsu(i) x(j)],[yrsu(i) y(j)],'b-');
        end
    end
end

%Creaci?n de las Circunferencias
for i=1:length(xrsu)
     o=-pi:0.01:pi;
     plot(0.2*cos(o)+xrsu(i),0.2*sin(o)+yrsu(i),':m','linewidth',2)
    pause(1);
end


hold off

