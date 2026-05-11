GET  /                        health check

GET  /status                  current config + last heartbeat
     ?account_id=xxx

POST /admin/set_active        change symbol/broker/mode
     {symbol, broker, mode}

POST /mt5/heartbeat           EA sends every 5s
     {account_id, broker, symbol, equity, balance,
      free_margin, spread_points, open_positions}
     → {server_mode, active_symbol, message}

GET  /mt5/next_signal         EA polls every 2s
     ?account_id&broker&symbol&equity&open_positions
     &candles_m5_json&candles_m15_json&candles_h1_json
     → SignalResponse

POST /mt5/event               EA reports fills/closes
     {account_id, signal_id, event_type, symbol,
      direction, volume, open_price, close_price,
      profit, detail}

POST /screenshot/analyze      upload chart image
     FormData(file, symbol, timeframe, account_id)
     → {command:"NO_TRADE", explanation, plan}
