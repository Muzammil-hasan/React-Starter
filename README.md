# React-Starter

# only for linux

1. Download project's zip file or clone it

2. Open folder in your IDE

3. Go to `webpack.mix.js`

4. Change the name of virtual host

5. Go to the directory if this is `make-vhost.py` file isn't in your project's home directory

6. Run these commands

```
// Change your virtul host name and add .local in end like my virtual host name is react-starter
// If your project directory is in another folder change the path like home/projects/react-starter

sudo python3 make-vhost.py react-starter.local /var/www/html/react-starter/



// Now reload apache2
systemctl reload apache2

```

7. Now go to your IDE terminal and install React and other dependicies by running

```
npm i --save-dev react react-dom @babel/preset-react
npm i


```

8. At last compile by `npm mix`
