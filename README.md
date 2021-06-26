# React-Starter for Linux

1. Download project's zip file or clone it

2. Open folder in your IDE

3. Go to `webpack.mix.js` and change virtual host name your project name

4. Go to the directory if `make-vhost.py` file isn't in your project's home directory

5. Run these commands

```
// Change your virtul host name and add .local in end like my virtual host name is react-starter
// If your project directory is in another folder change the path like home/projects/react-starter

sudo python3 make-vhost.py react-starter.local /var/www/html/react-starter/



// Now reload apache2

systemctl reload apache2

```

6. Now go to your IDE terminal and install React and other dependicies by running

```
npm i --save-dev react react-dom @babel/preset-react
npm i


```

7. At last compile by

```
npm mix


```
