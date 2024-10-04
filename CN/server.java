import java.io.*;
import java.net.*;
import java.util.*;
public class Echoserver
{
    public static void main (strings args[])
    { 
        try
        {
            serverSocket ss=new serverSocket(6666);
            Socket s=ss.accept();
            DataInputStream din =new DataInputStream (s.getInputStream());
            DataOutputStream dout=new DataOutputStream (s.getOutputStream());
            Scanner input=new Scanner(System.in);
            String senddata="";
            String receivedata="";
            while(!receivedata.equals("stop"))
            {
                receivedata=din.readUTF();
                System.out.println("client says:"+ receivedata);
                dout.write UTF(receivedata);
            }
            din.close()
            dout.close();
            s.close();
            ss.close();
        }
        catch(Execption e)
        {
            System.out.println(e);
        }
    }
    
}