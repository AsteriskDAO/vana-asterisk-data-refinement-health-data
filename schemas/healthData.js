
const profileSchema = new mongoose.Schema({
  age_range: {
    type: String,
    enum: ['18-20', '20-25', '25-30', '30-35', '35-40', '40-45', '45-50', '50+']
  },
  ethnicity: String,
  location: String,
  is_pregnant: Boolean
})


const healthDataSchema = new mongoose.Schema({
  healthDataId: { type: String, required: true },
  user_hash: { type: String, required: true },
  research_opt_in: { type: Boolean, default: false },
  profile: profileSchema,
  conditions: { type: [String] },
  medications: { type: [String] },
  treatments: { type: [String] },
  caretaker: { type: [String] },
  timestamp: { type: Date, default: Date.now }
})

// https://blue-yummy-rooster-621.mypinata.cloud/ipfs/bafkreiccdfvyk4mcaplnoof6edtwxe65ibozkdl355t3lbjikj3aaez3r4
/*
50 
Health Data Refiner
https://blue-yummy-rooster-621.mypinata.cloud/ipfs/bafkreiccdfvyk4mcaplnoof6edtwxe65ibozkdl355t3lbjikj3aaez3r4
https://github.com/Boka44/vana-asterisk-data-refinement-health-data/releases/download/v3/refiner-3.tar.gz
0x04fdb1b931c1c61849105a11f02a6c1519ad5e248d682ce2f65351453ff42523f10b98f1d9cd1fe3f47cfe4223c827a4401fd4dda7c23c3bec7dc59359af9974a1