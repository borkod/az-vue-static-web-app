<template>
  <div>
    <p>Message: {{ message }}</p>
    <p>Req: {{ req }}</p>
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      message: "",
      req: ""
    };
  },
  async mounted() {
    const resp = await (await fetch("/api/message")).json();
    this.message = resp.text;
    this.req = resp.req
  }
};
</script>