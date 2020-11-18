<template>
  <div v-if="isDrizzleInitialized" id="app">
    <h1>Property #{{ getPropertyFromId[0] }}</h1>
    <p>Address: {{ getPropertyFromId[1] }}</p>
    <p>Length: {{ getPropertyFromId[2] }}</p>
    <p>Width: {{ getPropertyFromId[3] }}</p>
  </div>
  <div v-else>
    Loading application...
  </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "Property",
  data: () => ({
    tokenId: null,
  }),
  computed: {
    ...mapGetters("drizzle", ["drizzleInstance", "isDrizzleInitialized"]),
    ...mapGetters("contracts", ["getContractData"]),

    getPropertyFromId() {
      let data = this.getContractData({
        contract: "PropertyPool",
        method: "getPropertyFromId",
        methodArgs: [this.tokenId],
      });
      if (data === "loading") return false;
      return data;
    },
  },
  // Register smart contract before the component mounts to ensure data is available
  created() {
    this.tokenId = this.$route.params.tokenId;
    this.$store
      .dispatch("drizzle/REGISTER_CONTRACT", {
        contractName: "PropertyPool",
        method: "getPropertyFromId",
        methodArgs: [this.tokenId],
      })
      .catch(() => {
        console.log("Error occured");
      });
  },
};
</script>
