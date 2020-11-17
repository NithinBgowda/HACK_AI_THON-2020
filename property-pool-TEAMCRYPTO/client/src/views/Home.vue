<template>
  <div v-if="isDrizzleInitialized" id="app">
    <h1>All Properties</h1>
    <ul v-if="getAllProperties">
      <router-link
        v-for="(property, i) in getAllProperties"
        :key="i"
        :to="`/p/${i}`"
      >
        {{ property[0] }}
        {{ property[1] }}
        {{ property[2] }}
        {{ property[3] }}
      </router-link>
    </ul>
  </div>
  <div v-else>
    Loading application...
  </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "Home",
  computed: {
    ...mapGetters("drizzle", ["drizzleInstance", "isDrizzleInitialized"]),
    ...mapGetters("contracts", ["getContractData"]),

    getAllProperties() {
      let data = this.getContractData({
        contract: "PropertyPool",
        method: "getAllProperties",
      });
      if (data === "loading") return false;
      return data;
    },
  },
  // Register smart contract before the component mounts to ensure data is available
  created() {
    this.$store.dispatch("drizzle/REGISTER_CONTRACT", {
      contractName: "PropertyPool",
      method: "getAllProperties",
      methodArgs: [],
    });
  },
};
</script>
