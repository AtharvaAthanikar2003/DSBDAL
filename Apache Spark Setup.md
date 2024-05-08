# Apache Spark Installation Instructions

Follow these steps to install Apache Spark on your system:

1. Navigate to your Downloads directory:
   ```
   cd Downloads/
   ```

2. Check the contents of the directory:
   ```
   ls
   ```

3. Clear the terminal for better visibility:
   ```
   clear
   ```

4. Download the Spark distribution:
   ```
   wget https://downloads.apache.org/spark/spark-3.5.1/spark-3.5.1-bin-hadoop3-scala2.13.tgz
   ```

5. List the contents of the directory to confirm the download:
   ```
   ls
   ```

6. Extract the downloaded Spark archive:
   ```
   tar -xzf spark-3.5.1-bin-hadoop3.tgz
   ```

7. List the contents again to verify extraction:
   ```
   ls
   ```

8. Rename the extracted directory for convenience (optional):
   ```
   mv spark-3.5.1-bin-hadoop3 spark
   ```

9. List the contents to confirm the renaming:
   ```
   ls
   ```

10. Change directory to the Spark folder:
    ```
    cd spark/
    ```

11. Print the current working directory to copy the path to clipboard:
    ```
    pwd | clip
    ```

12. Edit the .bashrc file to set environment variables using Vim:
    ```
    vim ~/.bashrc
    ```

13. Add the following lines at the end of the file, replacing `<paste_path_here>` with the copied path:
    ```
    export SPARK_HOME=<paste_path_here>
    export PATH=$PATH:$SPARK_HOME/bin
    ```

14. Save the changes and exit Vim by pressing `Esc`, then typing `:wq` and pressing `Enter`.

15. Return to the home directory:
    ```
    cd
    ```

16. Navigate to your desired directory (optional):
    ```
    cd Pranav-ubuntu/DSBDAL/
    ```

17. Check the contents of the directory (optional):
    ```
    ls
    ```

## Main code starts here

1. Create an input file for Spark processing by echoing a random sentence into a file named `input.txt`:
    ```
    echo "The quick brown fox jumps over the lazy dog" > input.txt
    ```

2. View the contents of the input file to verify creation:
    ```
    cat input.txt
    ```

3. Start the Spark shell:
    ```
    spark-shell
    ```

4. Run your Spark commands for data processing, such as:
    ```
    var a = sc.textFile("input.txt").flatMap(line=> line.split(" ")).map(word => (word,1));
    var b = a.reduceByKey(_ + _);
    b.collect foreach(println)
    ```

These steps will guide you through the installation process and demonstrate how to utilize Spark for data analysis and processing.
