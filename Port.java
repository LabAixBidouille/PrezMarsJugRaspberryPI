import gnu.io.*;
import java.io.PrintStream;
import java.io.IOException;

public class Port{

	SerialPort serialPort = null;
	PrintStream output = null;

	public Port(){
		try{
			CommPortIdentifier portId = CommPortIdentifier.getPortIdentifier("/dev/ttyUSB0");
			serialPort = (SerialPort) portId.open("Jug Mail", 5000);
		
			serialPort.setSerialPortParams(	9600,
											SerialPort.DATABITS_8,
											SerialPort.STOPBITS_1,
											SerialPort.PARITY_NONE);

			serialPort.setFlowControlMode(SerialPort.FLOWCONTROL_NONE);

			output = new PrintStream(serialPort.getOutputStream(), true);
		}
		catch(NoSuchPortException e){
			System.err.println("Le Port n'est pas disponible.");
		}
		catch(PortInUseException e){
			System.err.println("Le port est utilisé");
		}
		catch(UnsupportedCommOperationException e){
			System.err.println("Paramètrage non supporté");
		}
		catch(IOException e){
			System.err.println(e.getMessage());
			close();
		}
	}

	public void close(){
		serialPort.close();
	}

	public PrintStream getOutputStream(){
		return output;
	}

	static public void main(String[] args){
		Port p = new Port();

		System.out.println("Envoi message");
		p.getOutputStream().print("1");

		p.getOutputStream().print("0");
		//p.getOutputStream().flush();

		p.close();
	}
}
