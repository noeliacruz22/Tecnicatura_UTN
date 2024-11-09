<script setup>
import NavBar from './components/icons/NavBar.vue'; 
</script>

<template>
  <header>
    <!--barra de navegacion-->
    <NavBar />
    <main>
        <section id="educacion">
          <h2>Educación - Cursos</h2>
          <!--Componente Educación-->
          <Educacion />
        </section>
        <section id="experiencia">
            <h2>Experiencia</h2>
            <!--Componente Experiencia-->
            <ExperienciaComponente />
        </section>
        <section id="proyectos">
            <h2>Proyectos</h2>
            <!--Componente Proyectos-->
            <ProyectosComponente />
        </section>
        <section id="habilidades">
            <!--Componente Habilidades-->
            <h2>Habilidades</h2>
            <HabilidadesComponente />
        </section>
        <section id="intereses">
            <!--Componente Intereses-->
            <h2>Intereses</h2>
            <InteresesComponente />
        </section>
    </main>

  </header>


</template>

<style scoped>



</style>
