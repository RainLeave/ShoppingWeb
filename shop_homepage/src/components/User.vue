<template>
  <div id="user">
    {{ page_info }}
    <br>
    {{django_message}}
  </div>
</template>

<script>
export default {
  name: 'User',
  data () {
    return {
      page_info: 'This is User Page',
      django_message: ''
    }
  },
  mounted () { // ES6写法
    this.$axios.get('http://127.0.0.1:8000/api/v1/accounts/test/')
      .then(response => {
        // console.log(response.data)
        // this表示 指向
        this.django_message = response.data.message
      })
  }
}
</script>

<stype scoped>

</stype>
