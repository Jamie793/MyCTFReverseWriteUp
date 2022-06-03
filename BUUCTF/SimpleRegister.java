public class SimpleRegister{
    public static void main(String[] args) {

        char[] x = "dd2940c04462b4dd7c450528835cca15".toCharArray();
                    x[2] = (char)(x[2] + x[3] - 50);
                    x[4] = (char)(x[2] + x[5] - 0x30);
                    x[30] = (char)(x[0x1F] + x[9] - 0x30);
                    x[14] = (char)(x[27] + x[28] - 97);
                    int i;
                    for(i = 0; i < 16; ++i) {
                        char a = x[0x1F - i];
                        x[0x1F - i] = x[i];
                        x[i] = a;
                    }

        System.out.println(new String(x));
        
    }
}