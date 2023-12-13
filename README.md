# My GitHub Profile

Welcome to my GitHub profile! Below you can find some interactive elements.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your GitHub Profile</title>
    <style>
        body {
            margin: 0;
            overflow: hidden;
        }

        canvas {
            display: block;
        }

        /* Добавете други стилове, според вашите нужди */
    </style>
</head>
<body>
    <canvas id="canvas"></canvas>

    <script>
        const state = {
            fps: 60,
            color: "#0f0",
            charset: "0123456789ABCDEF",
            size: 10
        };

        const gui = new dat.GUI();
        const fpsCtrl = gui.add(state, "fps").min(1).max(120).step(1);
        gui.addColor(state, "color");
        gui.add(state, "charset");
        const sizeCtrl = gui.add(state, "size").min(1).max(120).step(1);

        const canvas = document.getElementById("canvas");
        const ctx = canvas.getContext("2d");

        let w, h, p;
        const resize = () => {
            w = canvas.width = window.innerWidth;
            h = canvas.height = window.innerHeight;

            p = Array(Math.ceil(w / state.size)).fill(0);
        };

        window.addEventListener("resize", resize);
        sizeCtrl.onFinishChange(() => resize());
        resize();
    </script>
</body>
</html>




(っ◔◡◔)っ ♥
👨‍💻 𝔽𝕦𝕝𝕝-𝕊𝕥𝕒𝕔𝕜 𝔻𝕖𝕧𝕖𝕝𝕠𝕡𝕖𝕣 | ℂ𝕠𝕕𝕖 𝔼𝕟𝕥𝕙𝕦𝕤𝕚𝕒𝕤𝕥 | 🎵 𝕄𝕦𝕤𝕚𝕔 𝕃𝕠𝕧𝕖𝕣 🐍 ℙ𝕪𝕥𝕙𝕠𝕟𝕚𝕤𝕥𝕒 | ℂ# 𝕊𝕙𝕒𝕣𝕡𝕤𝕙𝕠𝕠𝕥𝕖𝕣

📚 ℍ𝕠𝕣𝕣𝕠𝕣 & 𝕄𝕪𝕤𝕥𝕖𝕣𝕪 𝔹𝕠𝕠𝕜𝕨𝕠𝕣𝕞 🕵️‍♂️ 🔪 𝔼𝕩𝕡𝕝𝕠𝕣𝕚𝕟𝕘 𝕄𝕦𝕣𝕕𝕖𝕣𝕤, 𝕄𝕪𝕤𝕥𝕖𝕣𝕚𝕖𝕤 & 𝔹𝕝𝕠𝕠𝕕-ℂ𝕦𝕣𝕕𝕝𝕚𝕟𝕘 𝕋𝕒𝕝𝕖𝕤

🔲 🅳🅸🅶🅸🆃🅰🅻 🅰🆁🆃🅸🆂🆃 | ℙ𝕪𝕥𝕙𝕠𝕟 𝔾𝕣𝕒𝕡𝕙𝕚𝕔𝕤 𝕎𝕚𝕫𝕒𝕣𝕕 🖌️ 📐 ℂ𝕣𝕒𝕗𝕥𝕚𝕟𝕘 ℂ𝕣𝕖𝕒𝕥𝕚𝕧𝕖 ℂ𝕠𝕕𝕖 & 𝔾𝕣𝕒𝕡𝕙𝕚𝕔 𝔸𝕝𝕔𝕙𝕖𝕞𝕪 🎨

🌗 𝔼𝕞𝕓𝕣𝕒𝕔𝕚𝕟𝕘 𝕄𝕪 𝔻𝕦𝕒𝕝 ℕ𝕒𝕥𝕦𝕣𝕖 | 🏋️‍♂️ 𝔾𝕪𝕞 ℝ𝕒𝕥 & 🏡 ℍ𝕠𝕞𝕖𝕓𝕠𝕕𝕪

💡 𝕀𝕗 𝕪𝕠𝕦 𝕔𝕒𝕟 𝕕𝕣𝕖𝕒𝕞 𝕚𝕥, 𝕀 𝕔𝕒𝕟 𝕔𝕠𝕕𝕖 𝕚𝕥. 𝕃𝕖𝕥'𝕤 𝕔𝕣𝕖𝕒𝕥𝕖 𝕕𝕚𝕘𝕚𝕥𝕒𝕝 𝕞𝕒𝕘𝕚𝕔! ✨

𝕄𝕆𝕋𝕆 𝔾𝕀ℝ𝕃 🏍️♥

## I specialize in:

<p style="font-size: 1.2em; font-weight: bold; color: #2E4053; text-align: center; font-family: 'Arial', sans-serif; font-style: italic;">
  <b><i>Web Development | Software Engineering | Data Science | Cybersecurity | UI/UX Design |  Creativity | Digital Art</i></b>
</p>

<!-- Вграждане на HTML код в README.md -->
<img src="pics/code.png" alt="Code Logo" width="50"> <img src="pics/digital%20art.png" alt="Digital Art Logo" width="50"> <img src="pics/gimp.png" alt="GIMP Logo" width="50"> <img src="pics/incscape.png" alt="Inkscape Logo" width="50"> <a href="Games"><img src="pics/pngegg.png" alt="C# Logo" width="50"></a><a href="Py Codes"><img src="pics/python-5-logo-png-transparent.png" alt="Python Logo" width="50"></a> 

<p style="font-size: 1.2em; font-weight: bold; color: #2E4053; text-align: center; font-family: 'Arial', sans-serif; font-style: italic;">
  <b><i> You can test my projects by clicking the icons above 👀🔝</i></b>
</p>
