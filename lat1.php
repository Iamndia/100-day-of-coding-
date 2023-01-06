<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css" type="text/css">
    <title>LATIHAN</title>
</head>
<style>
    body{
        background-image: url(bg1.jpg);
        background-position: center;
        background-repeat: no-repeat;
        background-size: 100%;
        text-align: center;
    }
    .container{
        background-attachment: fixed;
        backdrop-filter: blur(2px);
        /* background-color: rgba(255, 255, 255, .15); */
    }
    legend{
        font-size: 20px;
        font-family: Georgia, 'Times New Roman', Times, serif;
    }
    title{
        font-family: Verdana, Geneva, Tahoma, sans-serif;
    }
    .bio{
        border: 1px solid #ddd;
        display: inline-block;
        padding: 2em;
        text-align: center;
        background-color: blur(50px);
        color: #fff;
        
    }
    .bio label{
        color: #333;     /* Warna: Purple */
        display: block;
        font-size: 12px;
        font-weight: bold;
        letter-spacing: 0.05em;
        margin-bottom: 5px;
    }
    .bio input[type="name"],
    .bio input[type="password"],
    .bio input[type="number"]{
        border: none;
        border-bottom: 1px solid #ddd;
        color: #333;
        font-size: 14px;
        margin-bottom: 15px;
        margin-left: 10px;
        padding: 0.5em 1em 0.5em 0;
    }
    .title{
        color: #fff;
    }
    .leg_bio{
        color: #fff;
    }
</style>
<body class="container">
    <h1><b class="title">FRAP REGISTRASI</b></h1>
    <div class="bio">
    <form action="" class="form">
        <fieldset>
            <legend class="leg_bio">Biodata</legend>
            <table>
                <tr>
                   <td>NIK</td>
                   <td>:</td>
                   <td><input type="number" name="number"><br></td>
                </tr>
                <tr>
                    <td>Nama</td>
                    <td>:</td>
                    <td><input type="name" name="nama_user"><br></td>
                </tr>
                <tr>
                    <td>JK</td>
                    <td>:</td>
                    <td><input type="checkbox" name="jenis_kelamin"><br></td>
                </tr>
                <tr>
                    <td>Alamat</td>
                    <td>:</td>
                    <td><textarea name="Alamat" id="" cols="20" rows="6"></textarea></td>
                </tr>
                <tr>
                    <td>TTl</td>
                    <td>:</td>
                    <td>
                        <select>
                            <option value="01">01</option>
                            <option value="02">02</option>
                            <option value="03">03</option>
                            <option value="04">04</option>
                            <option value="05">05</option>
                            <option value="06">06</option>
                            <option value="07">07</option>
                            <option value="08">08</option>
                            <option value="09">09</option>
                            <option value="10">10</option>
                            <option value="11">11</option>
                            <option value="12">12</option>
                            <option value="13">13</option>
                            <option value="14">14</option>
                        </select>
                        <select name="" id="">
                        <option value="">Januari</option>
                        </select>
                    </td>
                </tr>
            </table>
        </fieldset>
    </form>
    
    <form action=""></form>
    <fieldset>
        <legend>User Name</legend>
        <table>
            <tr>
                <td>User Name</td>
                <td>:</td>
                <td><input type="name" name="nama"></td>
            </tr>
            <tr>
                <td>Password</td>
                <td>:</td>
                <td><input type="password" name="nama"></td>
            </tr>
            <tr>
                <td>Email</td>
                <td>:</td>
                <td><input type="email" name="nama"></td>
            </tr>
        </table>
    </fieldset>
    </form>
    <form action="">
        <fieldset>
            <legend>Resolusi Tahun Ini</legend>
            <table>
                <tr>
                    <td><input type="checkbox">Menguasai Html</td>
                    <tr>
                        <td><input type="checkbox" value="">Kuliah</td>
                    </tr>
                    <tr>
                        <td><input type="checkbox">Bekerja</td>
                    </tr>
                </tr>
            </table>
        </fieldset>
        <br>
        <tr>
            <td><input type="submit" value="Kirim" name="submit"></td>
            <td></td>
            <td></td>
        </tr>
    </form>
    </div>
</body>
</html>