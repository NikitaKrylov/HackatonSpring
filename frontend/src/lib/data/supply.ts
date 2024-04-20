import type { Offer } from "./offer"

export type Supply = {
  id: number
  storage_id: number
  offers: Offer[]
  created_at: string
  supply_status: string
}
