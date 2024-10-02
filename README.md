# MyGrowMoney
Financial Management App

## Front-end

Follow the instructions below to run the front-end in a GitHub Codespace or locally.

### Codespaces

1. Create a GitHub Codespace in this repository.
2. Wait for Visual Studio Code in the Codespace to fully set up.
3. In Visual Studio Code, open the Terminal.
4. Change to the `front-end` directory:

    ```bash
    cd Front-end
    ```

5. Install the dependencies:

    ```bash
    npm install
    ```

6. Start the application:
    ```bash
    npm run dev
    ```

    By default, the application will run on port `5173`.

7. You're Ready! The front-end is now running, and you can start using the application at http://localhost:5173.

### Local

1. Clone the repository.

2. Change to the `front-end` directory:

    ```bash
    cd Front-end
    ```

3. Install the dependencies:

    ```bash
    npm install
    ```

4. Start the application:
    ```bash
    npm run dev
    ```

    By default, the application will run on port `5173`.

4. You're Ready! The front-end is now running, and you can start using the application at http://localhost:5173.

## Back-end

Follow the instructions below to run the back-end in a GitHub Codespace or locally.

### Codespaces

1. Create a GitHub Codespace in this repository.
2. Wait for Visual Studio Code in the Codespace to fully set up.
3. In Visual Studio Code, open the Terminal.
4. Change the active Java version to 21 using SDK MAN:
    ```bash
    sdk use java 21.0.4-ms
    ```

5. Optionally, check the current Java version:
    ```bash
    java --version
    ```
    The output should look similar to this:
    ```bash
    openjdk 21.0.4 2024-07-16 LTS
    OpenJDK Runtime Environment Microsoft-9889606 (build 21.0.4+7-LTS)
    OpenJDK 64-Bit Server VM Microsoft-9889606 (build 21.0.4+7-LTS, mixed mode, sharing)
    ```
6. Change to the `back-end` directory:
    ```bash
    cd Back-end
    ```
7. Start the application:
    ```bash
    mvn spring-boot:run
    ```
    By default, the application will run on port `8080`.
7. You're Ready! The back-end is now running, and you can start using the application at http://localhost:8080.

### Local

To run the back-end locally, ensure that you have Java 21 installed. You can use any OpenJDK distribution. Below are a few popular options:

- [Microsoft OpenJDK 21](https://learn.microsoft.com/en-us/java/openjdk/download#openjdk-21)
- [Amazon Corretto 21](https://docs.aws.amazon.com/corretto/latest/corretto-21-ug/downloads-list.html)
- [Oracle JDK 21](https://www.oracle.com/br/java/technologies/downloads/#java21)

Once you have Java 21 installed, follow these steps to run the back-end:

1. Clone the repository.

2. Change to the `back-end` directory:
    ```bash
    cd Back-end
    ```

3. Start the application:

    ```bash
    mvn spring-boot:run
    ```

    By default, the application will run on port 8080.

4. You're Ready! The back-end is now running, and you can start using the application at http://localhost:8080.

## Notes

You can run both the front-end and back-end in a single GitHub Codespace.