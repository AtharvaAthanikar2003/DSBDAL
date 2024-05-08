To install Apache Spark, follow these steps:

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

11. Print the current working directory to confirm the path:
    ```
    pwd
    ```

12. Edit the .bashrc file to set environment variables:
    ```
    sudo gedit ~/.bashrc
    ```

13. Add the following lines at the end of the file:
    ```
    export SPARK_HOME=/home/pranav/Downloads/spark
    export PATH=$PATH:$SPARK_HOME/bin
    ```

14. Save and close the file.

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

18. Open the input file for Spark processing (optional):
    ```
    vim input.txt
    ```

19. View the contents of the input file (optional):
    ```
    cat input.txt
    ```

20. Start the Spark shell:
    ```
    spark-shell
    ```

21. Run your Spark commands for data processing, such as:
    ```
    var a = sc.textFile("input.txt").flatMap(line=> line.split(" ")).map(word => (word,1));
    var b = a.reduceByKey(_ + _);
    b.collect foreach(println)
    ```

These steps will guide you through the installation process and demonstrate how to utilize Spark for data analysis and processing.
