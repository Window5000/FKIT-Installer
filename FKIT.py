import os

dir = "cd " + ". && "

print("Name: ", end='')
name = input()
os.system("npm init svelte " + name)
dir = "cd " + name + " && "
os.system(dir + "npm install")

file = open(name + "/src/routes/index.svelte", "w")
file.write("""<div class="hero min-h-screen bg-base-200">
    <div class="hero-content text-center">
      <div class="max-w-md">
        <h1 class="text-5xl font-bold">FCK IT</h1>
        <p class="py-6">"Bleeding Edge Tech Stack for 2025"</p>
        <a class="btn btn-primary" href="/getting-started/">Get Started</a>
      </div>
    </div>
  </div>""")

file = open(name + "/src/routes/getting-started.svelte", "w")
file.write("""<div class="hero min-h-screen bg-base-200">
    <div class="hero-content text-center">
      <div class="max-w-md">
        <h1 class="text-5xl font-bold">Getting Started</h1>
        <div class="divider"></div> 
        <a class="btn btn-primary" href="https://youtu.be/rFP7rUYtOOg" target="_blank">The Stack</a>
        <a class="btn btn-primary" href="https://svelte.dev/docs" target="_blank">Svelte</a>
        <a class="btn btn-primary" href="https://tailwindcss.com/docs/editor-setup" target="_blank">TailWIND</a>
        <a class="btn btn-primary" href="https://daisyui.com/" target="_blank">daisyui</a>
      </div>
    </div>
  </div>""")

file = open(name + "/src/routes/__layout.svelte", "w")
file.write("""<script>
	import '../app.css';
</script>

<slot />""")

os.system(dir + "npm install -D tailwindcss postcss autoprefixer svelte-preprocess")
os.system(dir + "npx tailwindcss init tailwind.config.cjs -p")
os.system(dir + "npm i daisyui")

with open(name + '/svelte.config.js', 'w') as file:
    file.writelines("""import adapter from '@sveltejs/adapter-auto';
import preprocess from "svelte-preprocess";

/** @type {import('@sveltejs/kit').Config} */
const config = {
    preprocess: [
        preprocess({
            postcss: true,
        }),
    ],
    kit: {
        adapter: adapter()
    }
};

export default config;""")

with open(name + '/tailwind.config.cjs', 'w') as file:
    file.writelines("""module.exports = {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {}
  },
  plugins: [require("@tailwindcss/typography"), require("daisyui")]
};""")

with open(name + '/src/app.css', 'w') as file:
    file.writelines("""@tailwind base;
@tailwind components;
@tailwind utilities;""")

with open(name + '/src/routes/__layout.svelte', 'w') as file:
    file.writelines("""<script>
	import '../app.css';
</script>

<slot />""")

os.system(dir + "npm install -D @tailwindcss/typography")