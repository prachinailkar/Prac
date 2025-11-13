/**
 * This is the main Java application used to test our C++ DLL.
 * * It does three things:
 * 1. Declares 'native' methods (add and subtract) that will be implemented in C++.
 * 2. Loads the compiled C++ DLL from the system.
 * 3. Runs a 'main' method to test the native functions and print the results.
 */
public class MathOperations {

    // 1. Declare the native methods.
    // The 'native' keyword tells Java that this method's implementation
    // is in a native library (like our C++ DLL).
    public native int add(int a, int b);
    public native int subtract(int a, int b);

    // 2. Load the native library (DLL).
    // This static block runs once when the class is loaded.
    // "MathNative" is the name of our DLL.
    // On Windows, the JVM will look for "MathNative.dll".
    static {
        try {
            System.loadLibrary("MathNative");
        } catch (UnsatisfiedLinkError e) {
            System.err.println("Native code library (MathNative.dll) failed to load.\n" +
                               "Make sure the DLL is in your java.library.path.");
            System.err.println(e);
            System.exit(1);
        }
    }

    // 3. The "application program to test it".
    public static void main(String[] args) {
        MathOperations calculator = new MathOperations();

        int a = 100;
        int b = 25;

        System.out.println("--- Java Test Application Running ---");
        System.out.println("Calling C++ DLL for math operations...");

        // Call the 'add' method implemented in C++
        int sum = calculator.add(a, b);
        System.out.println("Result of add(" + a + ", " + b + ") from C++: " + sum);

        // Call the 'subtract' method implemented in C++
        int difference = calculator.subtract(a, b);
        System.out.println("Result of subtract(" + a + ", " + b + ") from C++: " + difference);

        // Verification
        if (sum == (a + b) && difference == (a - b)) {
            System.out.println("\n--- Test SUCCESSFUL ---");
        } else {
            System.out.println("\n--- Test FAILED ---");
        }
    }
}