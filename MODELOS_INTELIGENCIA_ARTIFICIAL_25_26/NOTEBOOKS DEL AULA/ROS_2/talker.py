import rclpy  # importa la biblioteca rclpy, que es la biblioteca cliente de ROS 2 para Python
# importa la clase Node de rclpy.node, que es la clase base para todos los nodos en ROS 2
# Un nodo es una entidad que puede comunicarse con otros nodos mediante la publicación y suscripción a temas
from rclpy.node import Node 
# importa el tipo de mensaje String del paquete std_msgs. En ROS 2, los mensajes se definen en paquetes 
# y std_msgs es un paquete común que contiene tipos de mensajes estándar como String, Int32, etc.
from std_msgs.msg import String 


class Talker(Node): # define la clase Talker que hereda de Node

    def __init__(self): # el método constructor de la clase Talker
        super().__init__('talker') # llama al constructor de la clase base Node con el nombre del nodo 'talker'
        self.publisher_ = self.create_publisher(String, 'chatter', 10) # crea un publicador que publicará mensajes de tipo String en el tema 'chatter' con una cola de tamaño 10(se almacenan hasta 10 mensajes si el suscriptor no puede mantenerse al día)
        self.timer = self.create_timer(1.0, self.timer_callback) # crea un temporizador que llamará a la función timer_callback cada 1 segundo
        self.counter = 0 # inicializa un contador para llevar la cuenta de los mensajes publicados

    def timer_callback(self): # define la función que se llamará cada vez que el temporizador expire
        msg = String() # crea una instancia del mensaje String
        msg.data = f'Hola ROS2! Mensaje número {self.counter}' # asigna un valor al campo data del mensaje, que es una cadena de texto que incluye el número del mensaje
        self.publisher_.publish(msg) # publica el mensaje en el tema 'chatter'
        self.get_logger().info(msg.data) # registra un mensaje informativo en el registro del nodo, mostrando el contenido del mensaje publicado
        self.counter += 1 # incrementa el contador de mensajes


def main(args=None): # define la función principal que se ejecutará cuando se inicie el nodo
    rclpy.init(args=args) # inicializa la biblioteca rclpy
    node = Talker() # crea una instancia del nodo Talker
    rclpy.spin(node) # entra en un bucle que mantiene el nodo en ejecución y procesa las llamadas de retorno (callbacks)
    node.destroy_node() # destruye el nodo cuando se sale del bucle
    rclpy.shutdown() # apaga la biblioteca rclpy


if __name__ == '__main__':  # ejecuta la función main si este archivo se ejecuta como un script principal
    main() # llama a la función main
