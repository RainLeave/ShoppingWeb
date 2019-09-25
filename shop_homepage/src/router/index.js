// import Vue from 'vue'
// import Router from 'vue-router'
// import HelloWorld from '@/components/Home'

// Vue.use(Router)

// export default new Router({
//  routes: [
//    {
//     path: '/',
//      name: 'HelloWorld',
//      component: HelloWorld
//    }
//  ]
// })
import Vue from 'vue'
import Router from 'vue-router'
import home from '@/components/Home'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import User from '@/components/User'

Vue.use(ElementUI)
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: home
    },
    {
      path: '/user',
      name: 'User',
      component: User
    }
  ]
})
