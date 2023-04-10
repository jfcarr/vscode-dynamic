<html>

<head>
    <title>PHP Test</title>
</head>

<body>
    <?php
    class MyClass
    {
        /**
         * This function says hello.
         */
        function say_hello($name)
        {
            echo 'Hello, ' . $name  . '!';
        }

        /**
         * This function shows PHP info.
         */
        function show_info()
        {
            phpinfo();
        }
    }

    $myClass = new MyClass();

    $myClass->say_hello('Jim');
    $myClass->show_info();
    ?>
</body>

</html>