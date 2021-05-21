<template>
  <div>
    <tr>
      <th scope="row">{{ review.movie }}</th>
      <td>{{ review.title }}</td>
      <td>{{ review.user }}</td>
      <td>{{ review.updated_at }}</td>
    </tr>
  </div>
</template>

<script>
export default {
  name: 'ReviewPageItem',
  props: {
    review: {
      type: Object
    }
  },

}
</script>

<style>

</style>